class News:
    '''
    News class to define News Objects
    '''

    def __init__(self,id, name, description, url, category, language, country,image):
        self.id =id
        self.name = name
        self.description = description
        self.url = url
        self.category = category
        self.language = language
        self.country = country
        self.image = image