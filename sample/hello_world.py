from psbody.meshlite import Mesh, MeshViewer
from os.path import dirname

def main():
    fdir = dirname(__file__)
    mesh = Mesh(filename='%s/teapot.obj' % fdir)
    mv = MeshViewer()
    mv.dynamic_meshes = [mesh]

    print "~~\nThis should display a MeshViewer window with a teapot"
    print "You can click and drag on the window to rotate around the mesh."
    print "Press enter to continue. This will save the mesh as an obj file to your /tmp folder.\n~~\n"
    raw_input()

    outname = '/tmp/teapot.obj'
    mesh.write_obj(outname)
    print 'Saved file: ', outname


if __name__ == '__main__':
    main()


