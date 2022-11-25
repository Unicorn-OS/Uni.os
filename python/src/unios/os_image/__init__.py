class OSImage:
    def __init__(self, name):
        self.name = name
        self.image = ""

    from .lookup import lookup_ubuntu_iso
    from .default_list import default_list

    def image_from_name(self):
        return OSImage.lookup_ubuntu_iso(self.name)
