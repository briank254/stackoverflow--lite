
import hashlib

def id_generator(to_gen):
    """
    ID generator
    :params: to_gen: the string you want to generate an ID form
    :return: generated_id_value: the id generated from gen_name after message digest
    """
    gen_id = hashlib.md5()
    gen_id.update(to_gen.encode('utf8'))
    generated_id_value = int(str(int(gen_id.hexdigest(), 16))[0:12])
    return generated_id_value

