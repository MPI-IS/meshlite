# Copyright (c) 2017 Max Planck Society. All rights reserved.
# see accompanying LICENSE.txt file for licensing and contact information
# Created by Matthew Loper on 2013-02-20.


import numpy as np


def landm_xyz_linear_transform(self, ordering=None):
    from .utils import col, sparse

    landmark_order = ordering if ordering else self.landm_names
    # construct a sparse matrix that converts between the landmark pts and all vertices, with height (# landmarks * 3) and width (# vertices * 3)
    if hasattr(self, 'landm_regressors'):
        landmark_coefficients = np.hstack([self.landm_regressors[name][1] for name in landmark_order])
        landmark_indices = np.hstack([self.landm_regressors[name][0] for name in landmark_order])
        column_indices = np.hstack([col(3 * landmark_indices + i) for i in range(3)]).flatten()
        row_indices = np.hstack([[3 * index, 3 * index + 1, 3 * index + 2] * len(self.landm_regressors[landmark_order[index]][0]) for index in np.arange(len(landmark_order))])
        values = np.hstack([col(landmark_coefficients) for i in range(3)]).flatten()
        return sparse(row_indices, column_indices, values, 3 * len(landmark_order), 3 * self.v.shape[0])
    elif hasattr(self, 'landm'):
        landmark_indices = np.array([self.landm[name] for name in landmark_order])
        column_indices = np.hstack(([col(3 * landmark_indices + i) for i in range(3)])).flatten()
        row_indices = np.arange(3 * len(landmark_order))
        return sparse(row_indices, column_indices, np.ones(len(column_indices)), 3 * len(landmark_order), 3 * self.v.shape[0])
    else:
        return np.zeros((0, 0))


@property
def landm_xyz(self, ordering=None):
    landmark_order = ordering if ordering else self.landm_names
    landmark_vertex_locations = (self.landm_xyz_linear_transform(landmark_order) * self.v.flatten()).reshape(-1, 3) if landmark_order else np.zeros((0, 0))
    if landmark_order:
        return dict([(landmark_order[i], xyz) for i, xyz in enumerate(landmark_vertex_locations)])
    return {}


def recompute_landmark_indices(self, landmark_fname=None, safe_mode=True):
    filtered_landmarks = dict(filter(lambda e, : e[1] != [0.0, 0.0, 0.0], self.landm_raw_xyz.items()) if (landmark_fname and safe_mode) else self.landm_raw_xyz.items())
    if len(filtered_landmarks) != len(self.landm_raw_xyz):
        print "WARNING: %d landmarks in file %s are positioned at (0.0, 0.0, 0.0) and were ignored" % (len(self.landm_raw_xyz) - len(filtered_landmarks), landmark_fname)

    self.landm = {}
    self.landm_regressors = {}
    if filtered_landmarks:
        landmark_names = filtered_landmarks.keys()
        closest_vertices, _ = self.closest_vertices(np.array(filtered_landmarks.values()))
        self.landm = dict(zip(landmark_names, closest_vertices))
        if len(self.f):
            face_indices, closest_points = self.closest_faces_and_points(np.array(filtered_landmarks.values()))
            vertex_indices, coefficients = self.barycentric_coordinates_for_points(closest_points, face_indices)
            self.landm_regressors = dict([(name, (vertex_indices[i], coefficients[i])) for i, name in enumerate(landmark_names)])
        else:
            self.landm_regressors = dict([(name, (np.array([closest_vertices[i]]), np.array([1.0]))) for i, name in enumerate(landmark_names)])


def set_landmarks_from_xyz(self, landm_raw_xyz):
    self.landm_raw_xyz = landm_raw_xyz if hasattr(landm_raw_xyz, 'keys') else dict((str(i), l) for i, l in enumerate(landm_raw_xyz))
    self.recompute_landmark_indices()


def set_landmarks_from_raw(self, landmarks):
    '''
    can accept:
    {'name1': [float, float, float], 'name2': [float, float, float], ...}
    {'name1': np.array([float, float, float]), 'name2': np.array([float, float, float]), ...}
    [[float,float,float],[float,float,float], ...]
    np.array([[float,float,float],[float,float,float], ...])
    [np.array([float,float,float]),np.array([float,float,float]), ...]
    {'name1': int, 'name2': int, ...}
    [int,int,int]
    np.array([int,int,int])
    '''
    landmarks = landmarks if hasattr(landmarks, 'keys') else dict((str(i), l) for i, l in enumerate(landmarks))

    if np.all(map(lambda x: hasattr(x, "__iter__") and len(x) == 3, landmarks.values())):
        landmarks = dict((i, np.array(l)) for i, l in landmarks.items())
        self.set_landmarks_from_xyz(landmarks)
    elif np.all(map(lambda x: isinstance(x, (int, long)), landmarks.values())):
        self.landm = landmarks
        self.recompute_landmark_xyz()
    else:
        raise Exception("Can't parse landmarks")
