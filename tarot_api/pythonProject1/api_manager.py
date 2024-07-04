import random
from config import api_key_free_list
from api_key_free import api_key_free


class APIKeyManager:
    def __init__(self):
        number_of_key = len(api_key_free_list)
        self.free_key_list = []
        for i in range(number_of_key - 1):
            self.free_key_list.append(api_key_free(api_key=api_key_free_list[i]))
        self.spare_key = api_key_free(api_key=api_key_free_list[number_of_key - 1])

    def get_key_and_model(self):
        random_key = random.choice(self.free_key_list)
        weights = [0.1, 0.1, 0.5, 0.11]
        random_model = random.choices([0, 1, 2, 3], weights, k=1)[0]
        # with open('random_output.txt', 'a', encoding='utf-8') as file:
        #     file.write(f"random model {random_model}\n")

        if random_key.is_available(random_model):
            # with open('output.txt', 'a', encoding='utf-8') as file:
            #     file.write("use random key")
            return random_key, random_model
        # else:
        # with open('output.txt', 'a', encoding='utf-8') as file:
        #     file.write(f"random model {random_model} is not available\n")
        # time_start_find_key = datetime.now()
        for i in self.free_key_list:
            for j in [2, 0, 1, 3]:
                if i.is_available(j):
                    # with open('output.txt', 'a', encoding='utf-8') as file:
                    #     file.write("find available key "+str(datetime.now()-time_start_find_key)+f"model{j}\n")
                    return i, j
        # with open('output.txt', 'a', encoding='utf-8') as file:
        #     file.write("using spare key\n")
        return self.get_spare_key_and_model()

    def get_spare_key_and_model(self):
        for i in [2, 0, 1, 3]:
            if self.spare_key.is_available(i):
                return self.spare_key, i


api_key_manager = APIKeyManager()
