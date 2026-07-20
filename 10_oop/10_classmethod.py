class ChaiOrder:
    def __init__(self, tea_type,sweetness,size):
        self.tea_type=tea_type
        self.sweetness=sweetness
        self.size=size
    
    @classmethod
    def from_dict(cls,order_dict):
        return cls(order_dict['tea_type'],order_dict['sweetness'],order_dict['size'])
    
    @classmethod
    def from_string(cls,order_string):
        tea_type,sweetness,size=order_string.split('-')
        return cls(tea_type,sweetness,size)
    
class ChaiUtils:
    @staticmethod
    def is_valid_size(size):
        return size in ['small','medium','large']
print(ChaiUtils.is_valid_size('medium'))
    
order1=ChaiOrder.from_dict({'tea_type':'Masala','sweetness':'medium','size':'large'})
order2=ChaiOrder.from_string('Gingwr-low-small')
order3=ChaiOrder('Large','low','large')
print(order1.__dict__)
print(order2.__dict__)
print(order3.__dict__)