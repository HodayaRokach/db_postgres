class image:
    def __init__(self,id,userid,image_name,image_before_processing,image_after_processing):
        self.id = id
        self.image_name = image_name
        self.userid = userid
        self.image_after_processing = self.image_to_bytes(image_after_processing)
        self.image_before_processing = self.image_to_bytes(image_before_processing)

    def image_to_bytes(image_path):
        with open(image_path, 'rb') as image_file:
            image_bytes = image_file.read()
        return image_bytes
