import re
import pymongo
from bson.objectid import ObjectId


FIELD_MAPPING: dict = {
    'org': 'org',
    'name': 'name',
    'species': 'sample.metadata.Microorganism',
    'sequence_type': 'sample.summary.sequence_type',
    'metadata': 'sample.metadata',  # Used to retrieve all metadata fields.
    'sampling_year': 'sample.metadata.Date_Sampling_YYYY',
    'country_term': {'$arrayElemAt': ['$sample.metadata.Country', 0]},
    'source_type_term': {'$arrayElemAt': ['$sample.metadata.Source_Type', 0]},
    'sampling_date': 'sample.metadata.Date_Sampling',
    'allele_profile': 'pipelines.chewiesnake.allele_profile',
}

class API:
    def __init__(self, connection_string: str, field_mapping: dict):
        self.connection = pymongo.MongoClient(connection_string)
        self.db = self.connection.get_database()
        self.field_mapping = field_mapping

    def get_samples(
        self,
        mongo_ids = None,
        species_name: str = None,
        fields: set = set(FIELD_MAPPING.keys())
    ):

        # Ensure we always have these two fields in the set
        fields.add('org')
        fields.add('name')

        pipeline = list()

        # Match
        match = dict()
        if mongo_ids:
            object_ids = [ObjectId(mongo_id) for mongo_id in mongo_ids]
            match['_id'] = { '$in': object_ids }
        species_field = FIELD_MAPPING['species']
        if species_name:
            match[species_field ] = species_name

        pipeline.append(
            {'$match': match}
        )

        # Projection
        projection = dict()
        for field in fields:
            if isinstance(FIELD_MAPPING[field], str):
                projection[field] = f"${FIELD_MAPPING[field]}"
            else:
                projection[field] = FIELD_MAPPING[field]

        pipeline.append(
            {'$project': projection
            }
        )

        return self.db.samples.aggregate(pipeline)


    def get_samples_from_keys(
        self,
        key_list:list,
        fields: set = set(FIELD_MAPPING.keys())
    ):

        # We cannot search on an empty key_list.
        if len(key_list) == 0:
            return [list(), list()]

        # Ensure we always have these two fields in the set
        fields.add('org')
        fields.add('name')

        pipeline = list()

        # Match
        """pipeline.append(
                {'$match': {'$or': key_list}}  # pymongo.errors.OperationFailure: $and/$or/$nor must be a nonempty array
        ) """

        # Projection - map only the desired fields
        projection = dict()
        for field in fields:
            if isinstance(FIELD_MAPPING[field], str):
                projection[field] = f"${FIELD_MAPPING[field]}"
            else:
                projection[field] = FIELD_MAPPING[field]
        
        pipeline.append(
            {'$project': projection
            }
        )

        command_cursor = self.db.samples.aggregate(pipeline)

        # Check if there are samples in key_list that was not found in MongoDB.
        """unmatched = list()
        for key_pair in key_list:
            match = False
            for mongo_doc in command_cursor:
                if mongo_doc['org'] == key_pair['org'] and mongo_doc['name'] == key_pair['name']:
                    match = True
                    break
            if match == False:
                unmatched.append(key_pair) """

        # MongoDB CommandCursor cannot rewind, so we make a new one
        return (self.db.samples.aggregate(pipeline), list())
