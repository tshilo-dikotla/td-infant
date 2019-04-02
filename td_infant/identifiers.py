from edc_identifier.simple_identifier import SimpleUniqueIdentifier


class KaraboScreeningIdentifier(SimpleUniqueIdentifier):

    random_string_length = 5
    identifier_type = 'screening_identifier'
    template = 'KB{device_id}{random_string}'
