import os
import yaml
import io




def get_dt(dt_name):
    base_dir = os.path.dirname(__file__)

    str = dt_name.split('.')[-1]
    dt_file_name = os.path.join(base_dir, str, dt_name).replace("\\", "/")
    if str == 'yml':
        with io.open(dt_file_name, "r", encoding='utf-8') as f:
            dt_file_name = yaml.load(f.read(),Loader=yaml.FullLoader)
    
    return dt_file_name, str



if __name__ == "__main__":
    file_name, file_type = get_dt("test_data.xlsx")
    print(file_type)



