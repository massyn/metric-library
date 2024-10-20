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

    def render_jina(self,template,data,output = None,fwfilter = None):
        frameworks = {}
        for fw in data['frameworks']:
            for i in data['frameworks'][fw]:
                data['frameworks'][fw][i]['framework'] = fw
                for m in data['metrics']:
                    for r in m['references']:
                        if r == i:
                            if not 'measures' in data['frameworks'][fw][i]:
                                data['frameworks'][fw][i]['measures'] = []
                            if not m['title'] in data['frameworks'][fw][i]['measures']:
                                data['frameworks'][fw][i]['measures'].append(m['title'])
                frameworks[i] = data['frameworks'][fw][i]

        template_dir = 'templates'
        env = Environment(loader=FileSystemLoader(template_dir)).get_template(template)
        result = env.render(metrics = data['metrics'],domains = data['domains'],frameworks = frameworks, fwfilter = fwfilter, thisfw = data['frameworks'].get(fwfilter,{}))
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
    M.render_jina('framework.html',data,'docs/iso27001-2013.md','ISO27001:2013')
    M.render_jina('framework.html',data,'docs/iso27001-2022.md','ISO27001:2022')
    M.render_jina('framework.html',data,'docs/nist-csfv20.md','NIST CSF v2.0')
