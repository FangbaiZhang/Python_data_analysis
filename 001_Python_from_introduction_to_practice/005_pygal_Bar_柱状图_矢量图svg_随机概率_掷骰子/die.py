 # -*- coding: cp936 -*-
# ��ϸ��P296
# ģ��Ͷ��һ��ɸ�ӽ������

from random import randint

class Die():
    """��ʾһ�����ӵ���"""
    
    def __init__(self, num_sides=6):
        """����Ĭ��Ϊ6��"""
        self.num_sides = num_sides
        
    def roll(self):
        """����һ��λ��1����������֮�������κ���"""
        return randint(1, self.num_sides)
        
        

            

