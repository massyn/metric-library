import yaml
import os
from jinja2 import Environment, FileSystemLoader


class Metrics:
    def __init__(self):
        print('init')

    def parse_yaml(self,path):
        data = { 'domains' : {} , 'metrics' : [] , 'frameworks' : {}}
        for r, d, f in os.walk(path):
            for file in f:
                fle = os.path.join(r, file).replace('\\','/')

                print(f"Reading {fle}")
                with open(fle,'rt',encoding='utf-8') as q:
                    d = yaml.safe_load(q)
                    for i in d:
                        if type(d[i]) == list:
                            data[i] += d[i]
                        elif type(d[i]) == dict:
                            data[i] = data[i] | d[i]
        return data

    def render_jina(self,template,data,output = None):
        frameworks = {}
        for fw in data['frameworks']:
            for i in data['frameworks'][fw]:
                data['frameworks'][fw][i]['framework'] = fw
                frameworks[i] = data['frameworks'][fw][i]
        template_dir = 'templates'
        env = Environment(loader=FileSystemLoader(template_dir)).get_template(template)
        result = env.render(metrics = data['metrics'],domains = data['domains'],frameworks = frameworks)
        if output is None:
            print(result)
        else:
            print(f"Writing {output}")
            with open(output,'wt',encoding='utf-8') as q:
                q.write(result)

    # def test_schema(self,data):
    #     with open('schema.yml','rt',encoding='utf-8') as q:
    #         schema = yaml.safe_load(q)

    #     for table in schema:
    #         print(f"Testing schema : {table}")

    #         for i in data[table]:
    #             for j in schema[table]:
    #                 d = schema[table][j]
                    
    #                 # == is this a mandatory field?
    #                 if d['not_null'] is True:
    #                     print(i)
    #                     print(f"schema test : {table}.{j} - not null = {j in i}")

if __name__=='__main__':
    M = Metrics()

    data = M.parse_yaml('metrics')

    M.render_jina('metrics.html',data,'docs/metrics.md')
