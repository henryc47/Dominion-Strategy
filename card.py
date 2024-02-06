class Card():
    def __init__(self,name : str,type : str ,cost_to_buy : int ,buy_power :int ,vp : int):
        self.name = name
        self.type = type
        self.cost_to_buy = cost_to_buy
        self.buy_power = buy_power
        self.vp = vp

copper = Card("Copper","Treasure",0,1,0)
silver = Card("Silver","Treasure",3,2,0)
gold = Card("Gold","Treasure",6,3,0)
estate = Card("Estate","Victory",2,0,1)
duchy = Card("Duchy","Victory",5,0,3)
province = Card("Province","Victory",8,0,6)
