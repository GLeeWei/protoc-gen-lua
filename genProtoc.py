import os, sys

current_dir = os.path.dirname(os.path.realpath(__file__))
PROTOC_ROOT = os.path.join(current_dir, "protoc")
PLUGIN_GEN_LUA = os.path.join(current_dir, "plugin/protoc-gen-lua.bat")

def gen_lua_proto(scrDir, desDir):
    print(scrDir)
    if False == os.path.isdir(desDir):
        os.makedirs(desDir)
    for fn in os.listdir(scrDir):
        if fn.endswith(".proto"):
            os.system('%s\protoc.exe --plugin=protoc-gen-lua=%s --lua_out=%s %s' % (PROTOC_ROOT, PLUGIN_GEN_LUA, desDir, fn))

if __name__ == '__main__':
    protoc_des_dir = current_dir
    protoc_src_dir = current_dir
    if 2 == len(sys.argv):
    	protoc_src_dir = sys.argv[1]
    	protoc_des_dir = sys.argv[2]

	gen_lua_proto(protoc_src_dir, protoc_des_dir)