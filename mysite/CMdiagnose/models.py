# -*- coding: utf-8 -*-
from django.db import models

class Body(models.Model):
    gum = models.CharField(max_length=200,default="normal", null=True, blank=True)
    lips = models.CharField(max_length=200,default="normal",null=True, blank=True)
    heart = models.CharField(max_length=200,default="normal",null=True, blank=True)
    head = models.CharField(max_length=200,default="normal",null=True, blank=True)
    liver = models.CharField(max_length=200,default="normal",null=True, blank=True)
    spleen = models.CharField(max_length=200,default="normal",null=True, blank=True)
    stomach = models.CharField(max_length=200,default="normal",null=True, blank=True)
    kidney = models.CharField(max_length=200,default="normal",null=True, blank=True)
    lips = models.CharField(max_length=200,default="normal",null=True, blank=True)
    face = models.CharField(max_length=200,default="normal",null=True, blank=True)
    nose = models.CharField(max_length=200,default="normal",null=True, blank=True)
    throat = models.CharField(max_length=200,default="normal",null=True, blank=True)
    pulse = models.CharField(max_length=200,default="normal",null=True, blank=True)
    general = models.CharField(max_length=2000,default="normal",null=True, blank=True)
    temperment = models.CharField(max_length=200,default="normal",null=True, blank=True)
    result = models.CharField(max_length=2000,default="normal",null=True, blank=True)

    def add_ref(self):
        return False

class Tongue(models.Model):
    body = models.OneToOneField(Body, on_delete=models.CASCADE, primary_key=True)
    tip = models.CharField(max_length=200,default="normal",null=True, blank=True)
    root = models.CharField(max_length=200,default="normal",null=True, blank=True)
    side = models.CharField(max_length=200,default="normal",null=True, blank=True)
    middle = models.CharField(max_length=200,default="normal",null=True, blank=True)
    fur = models.CharField(max_length=200,default="normal",null=True, blank=True)
    fluid = models.CharField(max_length=200,default="normal",null=True, blank=True)
    color = models.CharField(max_length=200,default="normal",null=True, blank=True)
    moisture = models.CharField(max_length=200,default="normal",null=True, blank=True)
    bottom = models.CharField(max_length=200,default="normal",null=True, blank=True)
    def check_(self):
        # self.color=str("_")
        # self.bottom=str("_")
        self.body.result=str("==============================================") + "\n" + "\n" + "\n"  + "舌象" + "\n" + "\n"
        if ("white" in self.color and "thick" in self.fur):
            self.body.result+="stomach cold--寒邪入胃"+ "\n" + "\n" 

        if ("yellow" in self.color and "thick" in self.fur):
            self.body.result+="stomach cold turn to fevor--寒邪化火"+ "\n" + "\n" 

        if ("black" in self.color and "thick" in self.fur):
            self.body.result+="stomach cold turn to severe fevor--热甚失治"+ "\n" + "\n" 

        if ("white" in self.color and "none" in self.fur and "moist" in self.moisture):
            self.body.result+="spleen faint and cold--脾胃虚寒"+ "\n" + "\n" 

        if ("white" in self.color and "none" in self.fur and "moist" in self.moisture\
            and ("white" in self.body.face or "white" in self.body.lips)):
            self.body.result+="spleen faint and cold--脾胃虚寒, \
            此或泄泻或受湿。脾无火力。速宜党参、焦术、木香、茯苓、炙草、乾姜、大枣以振之。"+ "\n" + "\n" 

        if ("black" in self.color and "thick" in self.fur and "crack" in self.fur and "dry" in self.moisture):
            self.body.result+="stomach cold turn to severe fevor--热甚失治"+ "\n" + "\n" 
        
        if (("yellow" in self.color or "yellow" in self.middle) and "thin" in self.fur ):
            self.body.result+="spleen fevor--脾热"+ "\n" + "\n" 

        if (("yellow" in self.color or "yellow" in self.middle) and "thick" in self.fur ):
            self.body.result+="stomach fevor--胃微热"+ "\n" + "\n" 

        if (("black" in self.color or "black" in self.middle) and \
            "thick" in self.fur and "crack" in self.fur and "dry" in self.moisture):
            self.body.result+="stomach severe fevor--胃大热"+ "\n" + "\n" 

        if (("black" in self.color or "black" in self.middle) and \
            "thick" in self.fur and "crack" in self.fur and \
                "dry" in self.moisture and "black" in self.body.gum \
                    and "black" in self.body.lips):
            self.body.result+="stomach severe fevor to broken--胃将蒸烂矣"+ "\n" + "\n" 

        if ("red" in self.tip or "burr" in self.tip ):
            self.body.result+="heart fevor--心热"+ "\n" + "\n" 

        if ("black" in self.color  and "moist" in self.moisture ):
            self.body.result+="kidney faint--肾虚" + "\n" + "\n" 

        if (("red" in self.color  or "purple" in self.color) and "none" in self.fur ):
            self.body.result+="kidney faint--肾虚"+ "\n" + "\n" 

        if ("reflective" in self.color  or ("dry" in self.bottom and "hate cold" in self.body.temperment) ):
            self.body.result+="kidney faint in severe--肾水亏极"+ "\n" + "\n" 

        if ("red" in self.side or "burr" in self.side ):
            self.body.result+="liver fevor--肝热"+ "\n" + "\n" 

        if ("red" in self.bottom and "thick" in self.fur):
            self.body.result+="stomach cold turn to severe fevor and lack water--火灼水亏"+ "\n" + "\n" 

        # self.body.save()
        strlist=""
        strlist=" " + "\n" + self.body.result + "\n" + str("========身體症狀辯證請結合上述舌象判斷==========") + "\n" + "\n"
        return strlist

class Cases(models.Model):
    facts = models.CharField(max_length=2000,default="nothing",null=True, blank=True)
    symptom = models.CharField(max_length=2000,default="nothing",null=True, blank=True)
    solution = models.CharField(max_length=2000,default="nothing",null=True, blank=True)
    marks = models.CharField(max_length=200,default="0",null=True, blank=True)
    reference = models.CharField(max_length=2000,default="nothing",null=True, blank=True)
    def case_check(self,body):

        factlist=[]
        factlist=[x.strip() for x in str(self.facts).replace('其症', '').replace('之症','').replace('症', '')\
        .replace('為', '').replace('脈必','').replace('脈','').replace('必','').replace('，', ',').replace('、', ',').replace('。', ',').replace('.', ',').split(',')]
        counter = 0
        for element in factlist:
            if element != '' and element in body.general:
                counter += 1
                # print('match found in')
                # print(counter)

        self.marks = counter/len(factlist)
        if '' in factlist:
            self.marks = counter/(len(factlist))
        if self.marks > 0.05:
            body.result+="匹配度 " +str(float(self.marks)*100) + " % \n"
            body.result+=self.symptom.replace('【','\n\n【').replace('】','】\n') + "\n\n\n" 
            body.result+=self.solution.replace('【','\n【').replace('】','】\n') + "\n"+ "\n"+ "\n"
            body.result+="================================================================="+ "\n"


    def case_checkext(self,body):

        factlist=[]
        factlist=[x.strip() for x in str(self.facts).replace('其症', '').replace('之症','').replace('症', '')\
        .replace('為', '').replace('脈必','').replace('脈','').replace('必','').replace('，', ',').replace('、', ',').replace('。', ',').replace('.', ',').split(',')]
        reflist=[]
        reflist=[x.strip() for x in str(str(self.solution)+str(self.reference)).replace('其症', '').replace('之症','').replace('症', '')\
        .replace('為', '').replace('脈必','').replace('脈','').replace('必','').replace('，', ',').replace('、', ',').replace('。', ',').replace('.', ',').split(',')]
        genlist=[]
        genlist=[x.strip() for x in str(body.general).split(',')]
        counter = 0
        for element in factlist:
            for genele in genlist:
                if genele != '' and element != '' and genele in element:
                    counter += 1
                    # print('match found in')
                    # print(counter)
        for element in reflist:
            for genele in genlist:
                if genele != '' and element != '' and genele in element:
                    counter += 1
        # self.marks = counter/len(factlist)
        # if '' in factlist:
        #     self.marks = counter/(len(factlist))
        # if self.marks > 0.05:
        if counter > 0:
            # body.result+="匹配度 " +str(float(self.marks)*100) + " % \n"
            if("【" in self.solution):
                body.result+="============================"+ self.solution.replace(self.solution[int(self.solution.find("【")):],'') +"====================================="+ "\n"
            else:
                body.result+="================================================================="+ "\n"
            body.result+=self.symptom.replace('【','\n\n【').replace('】','】\n') + "\n\n\n" 
            body.result+=self.solution.replace('【','\n【').replace('】','】\n') + "\n"+ "\n"+ "\n"
            if (self.reference is not None):
                body.result+=self.reference.replace('【','\n\n【').replace('】','】\n') + "\n\n\n" 
            # body.result+="================================================================="+ "\n"


    def case_check_ttgj(self,body,marks):


        if (marks == 'ttgj'):
            factlist=[]
            factlist=[x.strip() for x in str(self.facts).replace('其症', '').replace('之症','').replace('症', '')\
            .replace('為', '').replace('脈必','').replace('脈','').replace('必','').replace('，', ',').replace('、', ',').replace('。', ',').split(',')]
            counter = 0
            for element in factlist:
                if element != '' and element in body.general:
                    counter += 1
                    # print('match found in')
                    # print(counter)

            self.marks = counter/len(factlist)
            if '' in factlist:
                self.marks = counter/(len(factlist)-1)
            if self.marks > 0.05:
                body.result+="========================来源：汤头歌诀=============================="+ "\n"
                body.result+="匹配度 " +str(float(self.marks)*100) + " % \n"
                body.result+=self.symptom + "\n" 
                body.result+=self.solution + "\n"+ "\n"+ "\n"
                body.result+="========================来源：汤头歌诀=============================="+ "\n"+ "\n"

class Person(models.Model):
    body = models.OneToOneField(Body, on_delete=models.CASCADE)
    tongue = models.OneToOneField(Tongue, on_delete=models.CASCADE)
    def series_check(self):
        #卷一表里虚实寒热辨
        self.body.result=''
        resultlist=[]
        symptomlist=[]
        solutionlist=[]
        ###########
        # 外感風寒表虛汗出惡風。
        # 頭痛發熱。
        # 惡風乾嘔。
        # 苔白薄。
        # 脈浮弱或浮緩。
        boolist=[
        ('惡風' in self.body.general), \
        ('頭痛' in self.body.general), \
        ('鼻鳴' in self.body.general), \
        (('white' in self.tongue.color) and ('thin' in self.tongue.fur)),\
        ('發熱' in self.body.general), \
        ('乾嘔' in self.body.general), \
        ('脈浮弱' in self.body.general), \
        ('脈浮緩' in self.body.general), \
        ]

        counter = 0
        for element in boolist:
            #print (element)
            if element==True:
                counter+=1
              #  print ('check counter inside loop' + str(counter))
        symptomlist.append('此病之在表')
        resultlist.append(float(counter/len(boolist)))
        solutionlist.append('参考药方： 桂枝去皮9克(3兩)  白芍9克(3兩)  甘草炙6克(2兩)  生薑切9克(3兩)  大棗擘12枚   ')
        
        ################

        for i in range(len(resultlist)):
            if resultlist[i] > 0.5 : # the severeness of the diagnose
                # print (symptomlist[i])
                # print (resultlist[i])
                # print (solutionlist[i])
                self.body.result=(symptomlist[i]) + "\n"
                self.body.result+=(str(resultlist[i])) + "\n"
                self.body.result+=(solutionlist[i])

# class Symptoms(models.Model):
#     whole = models.TextField(max_length=20000,default="",null=True, blank=True)
# class Diagnose:
#     def check(self, tonge):
#         if ("white" in tonge.color and "thick" in tonge.fur):
#             tonge.body.result="stomach cold--寒邪入胃"
#             return tonge.body.result
class Yao(models.Model):
    name = models.CharField(max_length=200,default="nothing",null=True, blank=True)
    responses = models.CharField(max_length=2000,default="nothing",null=True, blank=True)
    properties = models.CharField(max_length=2000,default="nothing",null=True, blank=True)
    def yao_check(self,body):

        factlist=[]
        factlist=[x.strip() for x in str(self.responses).replace('【性味歸經】', '').replace('【功效】',',')\
        .replace('，', ',').replace('、', ',').replace('。', ',').replace('.', ',').split(',')]
        counter = 0
        for element in factlist:
            if element != '' and element in body.general:
                counter += 1
                # print('match found in')
                # print(counter)

        self.marks = counter/len(factlist)
        # if '' in factlist:
        #     self.marks = counter/(len(factlist)-1)
        if self.marks > 0.05:
            body.result+=self.name + "匹配度 " +str(float(self.marks)*100) + " % \n"
            body.result+=self.responses.replace('center','p').replace('【','\n\n【').replace('】','】\n') + "\n\n\n" 
            body.result+=self.properties.replace('center','p').replace('【','\n【').replace('】','】\n') + "\n"+ "\n"+ "\n"


    def yao_checkext(self,body):

        factlist=[]
        factlist=[x.strip() for x in str(self.responses).replace('【性味歸經】', '').replace('【功效】',',')\
        .replace('，', ',').replace('、', ',').replace('。', ',').replace('.', ',').split(',')]
        reflist=[]
        reflist=[x.strip() for x in str(self.properties).replace('【性味歸經】', '').replace('【功效】',',')\
        .replace('，', ',').replace('、', ',').replace('。', ',').replace('.', ',').split(',')]
        genlist=[]
        genlist=[x.strip() for x in str(body.general).split(',')]
        genlist = [i for i in genlist if i]
        counter = 0
        for element in factlist:
            for genele in genlist:
                if genele != '' and element != '' and genele in element:
                    counter += 1
                    # print('match found in')
                    # print(counter)
        for element in reflist:
            for genele in genlist:
                if genele != '' and element != '' and genele in element:
                    counter += 1
        # self.marks = counter/len(factlist)
        # if '' in factlist:
        #     self.marks = counter/(len(factlist))
        # if self.marks > 0.05:
        if counter > 0:
            body.result+="================= "+self.name + " ================= "
            body.result+=self.responses.replace('center','p').replace('【','\n\n【').replace('】','】\n') + "\n\n\n" 
            body.result+=self.properties.replace('center','p').replace('【','\n【').replace('】','】\n') + "\n"+ "\n"+ "\n"


class Xue(models.Model):
    name = models.CharField(max_length=200,default="nothing",null=True, blank=True)
    responses = models.CharField(max_length=2000,default="nothing",null=True, blank=True)
    properties = models.CharField(max_length=2000,default="nothing",null=True, blank=True)


    def __str__(self):
        """A string representation of the model."""
        return self.name


    def xue_check(self,body):

        factlist=[]
        factlist=[x.strip() for x in str(self.responses).replace('【性味歸經】', '').replace('【功效】',',')\
        .replace('，', ',').replace('、', ',').replace('。', ',').replace('.', ',').split(',')]
        counter = 0
        for element in factlist:
            if element != '' and element in body.general:
                counter += 1
                # print('match found in')
                # print(counter)

        self.marks = counter/len(factlist)
        # if '' in factlist:
        #     self.marks = counter/(len(factlist)-1)
        if self.marks > 0.05:
            body.result+=self.name + "匹配度 " +str(float(self.marks)*100) + " % \n"
            body.result+=self.responses.replace('center','p').replace('【','\n\n【').replace('】','】\n') + "\n\n\n" 
            body.result+=self.properties.replace('center','p').replace('【','\n【').replace('】','】\n') + "\n"+ "\n"+ "\n"


    def xue_checkext(self,body):

        factlist=[]
        factlist=[x.strip() for x in str(self.responses).replace('【功效】',',')\
        .replace('，', ',').replace('、', ',').replace('。', ',').replace('.', ',').split(',')]
        reflist=[]
        reflist=[x.strip() for x in str(self.properties).replace('【功效】',',')\
        .replace('，', ',').replace('、', ',').replace('。', ',').replace('.', ',').split(',')]
        genlist=[]
        genlist=[x.strip() for x in str(body.general).split(',')]
        genlist = [i for i in genlist if i] 
        counter = 0
        for element in factlist:
            for genele in genlist:
                if (genele != '' and element != '' and genele in element) or genele in self.name:
                    counter += 1
                    # print('match found in')
                    # print(counter)
        for element in reflist:
            for genele in genlist:
                if (genele != '' and element != '' and genele in element) or genele in self.name:
                    counter += 1
        # self.marks = counter/len(factlist)
        # if '' in factlist:
        #     self.marks = counter/(len(factlist))
        # if self.marks > 0.05:
        if counter > 0:
            body.result+="================= "+self.name + " ================= "
            body.result+=self.responses.replace('center','p').replace('【','\n\n【').replace('】','】\n') + "\n\n\n" 
            body.result+=self.properties.replace('center','p').replace('【','\n【').replace('】','】\n') + "\n"+ "\n"+ "\n" + "</li>" + "</ul>"
        
        # print(set(genlist))

