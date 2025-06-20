import math


class Pagination():

    def __init__(self, lists, page_size= 10):
        if lists == None:
            lists = []
        self.lists = lists
        self.page_size = page_size
        self.current_idx = 0
        self.total_number_page = math.ceil(len(self.lists)/(self.page_size))

    def get_visible_items(self):
        start = self.current_idx * self.page_size
        end = start + self.page_size
        return self.lists[start:end]
    
    def go_to_page(self,page_num):
        if page_num < 1 or page_num > self.total_number_page:
            raise ValueError(f"Page number must be between 1 and {self.total_number_page}")
        self.current_idx = page_num - 1
        return self
    
    def first_page(self):
        self.current_idx = 0
        return self.current_idx
    
    def last_page(self):
        self.current_idx = self.total_number_page - 1
        return self
    
    def next_page(self):
        if self.current_idx < self.total_number_page - 1:
          self.current_idx += 1
        return self
    
    def previous_page(self):
        if self.current_idx > 0:
            self.current_idx -= 1
        return self
    
    def __str__(self):
        return '\n'.join(self.get_visible_items())

p = Pagination(['a', 'b', 'c', 'd', 'e', 'f', 'g'], page_size=3)

print(p.get_visible_items())  
p.current_idx = 1
print(p) 
print(p.get_visible_items())  
p.current_idx = 2
print(p) 
print(p.get_visible_items())
p.first_page()
print(p.get_visible_items())
p.next_page()
print(p.get_visible_items())  
p.last_page()
print(p.get_visible_items())
p.next_page()
print(p.get_visible_items())
p.previous_page()
print(p.get_visible_items())

 