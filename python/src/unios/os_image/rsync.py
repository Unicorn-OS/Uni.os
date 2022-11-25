import sysrsync

class Sync:
    @classmethod
    def find_node_with_OS(cls):
        pass

    @classmethod
    def sync_OS_image(cls):
        pass

    @classmethod
    def sync_OS_media(cls):
        sysrsync.run(source_ssh='10.0.0.160',
                     sync_source_contents=False,
                     source='/home/me/.uni/os/dl',
                     destination='/home/me/.uni/os/',
                     private_key="/home/me/.ssh/id_rsa",
                     options=['-a'])

