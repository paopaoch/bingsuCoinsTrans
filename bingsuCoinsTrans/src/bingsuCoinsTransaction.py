from pynamodb.models import Model
from pynamodb.attributes import UnicodeAttribute, NumberAttribute, UTCDateTimeAttribute
from pynamodb.indexes import GlobalSecondaryIndex, AllProjection
import os

class PynamoBingsuCoinsTrans(Model):
    ''' database to store user '''
    class Meta:
        table_name = os.environ.get('CARBON_COINS_TRANS_TABLE')
        region = 'ap-southeast-1'
    coin_transaction_id = UnicodeAttribute(hash_key = True)
    user_id = UnicodeAttribute()
    date_time = UnicodeAttribute()
    carbon_coins = NumberAttribute()
    
class CoinsIndex(GlobalSecondaryIndex):
    """
    This class represents a global secondary index
    """
    class Meta:
        index_name = 'date_time'
        read_capacity_units = 1
        write_capacity_units = 1
        # All attributes are projected
        projection = AllProjection()

    # This attribute is the hash key for the index
    # Note that this attribute must also exist
    # in the model
    date_time = UnicodeAttribute(hash_key=True)
    