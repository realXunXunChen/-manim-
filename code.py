from manimlib.imports import * 

class Party1(Graphic_Image):
    def construct(self):
        g1 = self.big_text("1840年")
        g2 = self.gi("这是一个让所有中国人都难以忘怀的日子","1")
        self.big_text("因为在这一天")
        self.gi_("2","西方列强用实力告诉了我们","天朝上国只是你们夜郎自大")
        self.gi("国与国之间还得靠实力说话","3")
        self.gi("风声雨声读书声","4")
        self.gi("那都不如枪炮声","5")
        self.gi("家事国事天下事","6")
        self.gi("今天都要变丧事","7")
        self.gi_("8","而这一切的起因","竟然是因为鸦片这样祸国殃民的玩意儿")

        self.two_fig("9","10","所以时至今日","毒品也是我国打击最严的犯罪之一")
        self.two_fig("11","12","比如海洛因50克死刑","一个鸡蛋的重量而已")
        self.gi("大英帝国用实力告诉我们","13")
        self.gi("打你纯粹是想获取利益","14")
        self.gi("顺便加上自由民主","15")
        self.gi_("16","所以大家看看今天","这一套还是这一套")
        self.gi("想打谁就说谁“不自由不民主”","17")
        self.gi("帝国主义的“民主”","18")
        self.gi("那真是失礼失礼佩服佩服","19")
        self.gi("所以以前流行一个段子","20")
        self.gi_("21","叫做帝国主义国家如果说你有","大规模杀伤性武器","你最好真有")
        self.gi("否则伊拉克，叙利亚，伊朗，利比亚这些国家便是下场","22")

        self.gi("《南京条约》签定之后","23")
        self.gi("那真是“一大波僵尸即将袭来”","24")
        self.gi("什么《虎门条约》《望厦条约》《黄埔条约》","25")
        self.two_fig("26","27","从此大清帝国的脑子和身体")
        self.gi("真的是一步一步的被蚕食了","28")
        self.gi_("29","最早开始进行反抗的是","太平天国运动")
        self.gi("大家知道太平天国运动为何可以如此声势浩繁","30")
        self.gi("若不是最后领导人的腐败内斗","31")
        self.gi("或许还真就推翻了大清帝国","32")

    def two_fig(self,image1,image2,*text):
        tex = [0 for i in range(len(text))]
        time = 0
        for i in range(len(text)):
            tex[i] = Graphic(text[i])
            time += len(text[i])*TIME_INTERVAL
        fig1 = ImageMobject(image1,media_dir,height = 4,width = 3)
        Cross(fig1)
        fig1.shift(3.5*LEFT)
        self.add(fig1)
        fig2 = ImageMobject(image2,media_dir,height = 4,width = 3)
        fig2.shift(3.5*RIGHT)
        self.add(fig2)
        for i in range(len(text)):
            self.play(Write(tex[i]), run_time = len(text[i])*TIME_INTERVAL)
            self.remove(tex[i])
        self.clear()
        
class Party2(Graphic_Image):
    def construct(self):
        node = [0 for i in range(50)]
        opium = self.mind_start(LEFT*5,"鸦片战争","鸦片战争之后")
        node[0] = self.mind_node(1,opium,"赔款","首先是赔款","累计应该是赔了2800万元左右")
        node[1] = self.mind_node(1,node[0][1],"收刮百姓","钱从哪来","当然是收刮百姓啦")
        node[2] = self.mind_node(0.5,node[1][1],"赋税","所以赋税加重")
        node[3] = self.mind_node(-0.5,node[1][1],"贪污腐败","再加上内部的贪污腐败","致使大量的横征暴敛")
        node[4] = self.mind_node(0,opium,"协定关税","还有就是英国人拥有了协定关税的权力")
        node[5] = self.mind_node(0.5,node[4][1],"倾销","所以英国人的工业品便来到了中国大量倾销")
        node[6] = self.mind_node(-0.5,node[5][1],"手工业者破产","对中国的男耕女织的生活造成了巨大的负面影响",
                "各种城乡手工业者更是频繁破产")
        node[7] = self.mind_node(-1,opium,"地主兼并土地","而我们的地主阶级则趁机大量兼并土地")
        node[8] = self.mind_node(-1,node[7][1],"产生大量贫民",
                "真是国家不幸土豪幸",
                "在这种民族矛盾与阶级矛盾双重加剧的情况下",
                "农民起义的暴发也是一种历史的必然")
        self.clear()

class Party3(Graphic_Image):
    def construct(self):
        self.gi("但是碍于小农阶级思想的狭隘性","33")
        self.gi("太平天国运动也在中外势力的联合绞杀下失败了（1864）","34")
        self.gi_("35","而第二次鸦片战争（1856~1860）","便在这期间发生了")
        self.gi("而我们的圆明园也被毁于这场战争","36")
        self.gi("无数珍宝都落于外敌之手","37")
        self.gi_("38","","时至今日",
                "英国的大英博物馆里面","还有陈列了许多在这个时期抢劫的物品")

        self.big_text("弱国无外交，落后就要挨打")
        self.gi("沙俄也趁机掠夺了我们很多的领土","39")
        self.gi_("40","大清为了维护其天朝上国的地位","就搞起来所谓“中学为体，西学为用”的洋务运动")
        self.gi("然而没有什么大用","41")

        self.gi("1894年的“甲午中日战争”让我们再次见识到了","42")
        self.gi("以慈禧太后为首的大清帝国的无能之至","43")
        self.gi("战后维新派搞了一个“维新变法”","44")
        self.gi("谭嗣同也牺牲于这场变法","45")
        self.gi("然而还是没用","46")
        self.gi_("47","到头来还是变成了别人","茶余饭后的谈资与街头巷尾的笑话")
        


        self.gi_("48","而其他人跑得跑逃得逃","甚至还有借救国之名","在国外招摇撞骗")
        self.gi_("49","广纳财物为自己娶了数房姨太太（多为少女）")
        self.gi_("50","为国还是为己","我是真的想不明白康有为之流","到底是为啥")
        self.gi_("51","后来章太炎讽刺他","国之将亡必有（妖孽 出自《礼记》）","老而不死是为（贼 出自《论语》）")
        self.gi_("52","我觉得他们与其说是为了国家","倒不如哗众取宠政治投机")
        self.gi_("53","脑子里面充斥着小资产阶级的思想","精致利己才是他们的本色")
        self.gi_("54","所以他们鄙视群众","惧怕群众脱离群众","不敢放手发动群众","他们也代表不了底层群众的利益")
        self.gi("对外做不到赶走列强","55")
        self.gi("对内做不到团结人民","56")
        self.gi("这也是他们失败的根本原因","57")

class Party4(Graphic_Image):
    def construct(self):

        self.gi_("58","《马关条约》签定之后")
        self.gi_("59","帝国主义国家都震惊了")
        self.gi_("60","你大清帝国号称自强求富")
        self.gi_("61","我们当你多牛逼来着","结果就这")
        self.gi_("62","弹丸之国的小日本都能把你屎给打穿")
        self.gi_("63","这简直就是一块行走在在路上的","毫无攻击力的小肥羊啊")
        self.gi_("64","我大灰狼不咬两口")
        self.gi_("65","那都对不起上帝的的栽培")
        self.gi_("66","更加对不起我们民主国家的威名","我们民主国家必须好好教育教育你们")
        self.gi_("67","你们天朝上国又软又香","不咬不行啊")
        self.gi_("68","你们天朝地大物博","给你们都浪费")
        self.gi_("69","还是我们民主国家来帮你们承担承担吧",
                "这一开口就是老民主国家了")
        self.gi_("70","西方国家凭借一己之力",
                "将“民主国家”从褒义词变成了贬义词")
        self.gi_("71","20世纪初这些民主国家",
                "就给我送来一份惊喜")
        self.gi_("72","《辛丑条约》的签定")
        self.gi_("73","管我们要了4.5亿两白银","实际算上利息超过9亿白银")
        self.gi_("74","以及要了各种权力","铁路权，内部驻军等等")
        self.gi_("75","而我们的老佛爷还说出了那句","惊世骇俗之言")
        self.big_text("量中华之物力，结于国之欢心")
        self.gi_("76","翻译过来就是","各位爷，本地盛产美女")
        self.gi_("77","欢迎过来白嫖啊","嫖一送一，直到您满意为止")
        self.gi_("78","凭借这句话","我觉得她比秦桧还禽兽不如")
        self.gi_("79","应该在圆明园遗址内给她","也立一个铜像")
        self.gi_("80","专门给人唾弃","耻辱，国之耻辱")


class Party5(Graphic_Image):
    def construct(self):
        tex = [0 for i in range(50)]
        self.gi_("81","为了救亡图存","1911年孙中山先生")
        self.gi_("82","发动了辛亥革命","致使清帝退位")
        self.gi_("83","我们也开始进入了中华民国","这个我们当下有一些年轻的孩子憧憬的时期")
        self.gi_("84","虽然实际上也可称为中国历史上","最黑暗的几个时期之一")
        self.gi_("85","辛亥革命只是名义上成功了","就是推翻了帝制")
        self.gi_("86","以后的人想称帝基本上都是找死","不得民心，谁想称帝都必然上下离心")
        tex[0] = self.flow_chart_start(LEFT*5+UP*2.5,"袁世凯","辛亥革命后中国实际的掌权人是袁世凯")
        tex[1] = self.flow_chart_right(0,tex[0],"军阀","而袁大头其实是一个军阀","还是个想要称帝的军阀")[1]
        tex[2] = self.flow_chart_right(0,tex[1],"四分五裂","称帝失败后逝去","其军阀势力四分五裂","情况复杂得要死")[1]
        tex[3] = self.flow_chart_right(1,tex[2],"黎元洪","什么黎元洪")[1]
        tex[4] = self.flow_chart_right(0,tex[2],"张勋","张勋")[1]
        tex[5] = self.flow_chart_right(-1,tex[2],"段祺瑞","段祺瑞")[1]
        tex[6] = self.flow_chart_right(-2,tex[2],"孙传芳","孙传芳")[1]
        tex[7] = self.flow_chart_right(-3,tex[2],"吴佩孚","吴佩孚")[1]
        tex[8] = self.flow_chart_right(-4,tex[2],"张作霖","张作霖等等")[1]
        tex[9] = self.flow_chart_down(0,tex[2],"一直存在","而且军阀这种东西的影响一直都存在","至少在新中国成立之前都是")[1]
        self.clear()
        
        tex[10] = self.flow_chart_start(LEFT*5+UP*2.5,"曾国潘(湘军)","军阀这种东西","源于曾国潘",
                "当年曾国潘平定太平天国运动","一时权势炙手可热")
        tex[11] = self.flow_chart_right(0,tex[10],"李鸿章(淮军)","曾国潘培养了李鸿章为接班人")[1]
        tex[12] = self.flow_chart_right(0,tex[11],"袁世凯(北洋新军)","李中堂培养了袁大头",
                "袁大头则是北洋新军的领导人")[1]
        self.big_text("大家从这里其实可以看出来")
        self.big_text("军阀权力的兴替")
        self.big_text("基本上都是从前面继承而来")
        self.clear()
        self.gi_("87","这就叫新事物脱胎于旧事物的母体之中")
        self.gi_("88","后面蒋委员长")
        self.gi("在本质上还是军阀吧","89")
        self.gi("蒋中正娶了宋美龄","90")
        self.gi("借助江浙商户的财力","91")
        self.gi("以及孙中山先生建立的北伐军","92")
        self.gi("继承了这种军阀","93")
        self.gi("所以他做不到令行禁止","94")
        self.gi("更加做不到与民同乐","95")
        self.gi_("96","而且还要经常与这些军阀博弈")
        self.gi_("97","只是常凯申实际治军治国水平稀松平常","就是政治手段比较牛逼")
        self.gi_("98","所以其实军阀对其的信任","到底不太高")

        self.gi_("99","总之袁大头死后","政府经常换")
        self.gi_("100","先是段祺瑞")
        self.gi_("101","到常凯申执政之前")
        self.gi_("102","还有一大堆奇怪的牛鬼蛇神")
        self.gi_("103","此时还有一个重要的事件要说","那就是一战后的“巴黎和会”")
        self.gi_("104","我们中国作为战胜国")
        self.gi_("105","却连走上谈判桌的权力都没有")
        self.gi_("106","这也引发中国历史上的第一次轰轰烈烈的学生运动","就是五四运动")
        self.gi_("107","这次运动既反对帝国主义")
        self.gi_("108","也反对封建主义")
        self.gi_("109","工人阶级也开始走向了政治舞台")
        self.gi_("110","此时俄国“十月革命”的胜利")
        self.gi_("111","马克思主义传入中国")
        self.gi_("112","李大钊就是中国第一位马克思主义者","也是毛泽东同志工作的介绍人")
        self.gi_("113","通过一系列的学生运动工人运动积累基础")
        self.gi_("114","后面到1921年的时候","中国共产党才开始成立")
        self.gi_("115","时至今日","中国共产党对中国的革命，建设与改革","已经进行了长达一百年的探索与实践")

        self.gi_("116","中共成立之初","主要就是去领导一些工人运动")
        self.gi_("117","以及和这些军阀型政府斗智斗勇")
        self.gi_("118","这些愿意下到基层的人是一类","比如说毛泽东同志")
        self.gi_("119","我们这些铁粉一般称之为教员")
        self.gi_("120","当年林彪同志等人要给教员安上")
        self.big_text("伟大的导师，伟大的领袖")
        self.big_text("伟大的统帅，伟大的舵手")
        self.big_text("这些称号")
        self.gi_("121","而毛泽东同志则不同意这些","因为他曾说：")
        self.big_text("因为我历来是当教员的")
        self.big_text("现在还是当教员")
        self.big_text("其他的一概辞去")
        self.gi_("122","我们这些铁粉尊重其愿望","一般称之为教员",
                "本视频后面也一律以教员","来称呼毛泽东同志")
        self.gi_("123","当然此时还有一部分的人","源于新文化运动")
        self.gi_("124","比如陈独秀","这部分人未曾去过基层")
        self.gi_("125","此时处于毛泽东思想的早期积累阶段")
        self.gi_("126","1922年孙中山先生")
        self.gi_("127","在对帝国主义的希望幻灭后")
        self.two_fig("128","129","接受了中共与苏联意见")
        self.gi_("130","提出联俄，联共，扶助农工的策略")
        self.gi_("131","此时孙中山先生也认识到了","西方列强唯利是图的本质")
        self.gi_("132","1924年国民党正式建立")
        self.gi_("133","中共以个人身份参与国民党")
        self.gi_("134","孙中山创建黄埔军校","培养军队进行北伐")
        self.gi_("135","北伐之前","中共主要在做的是组建工会，农会","成立可以直接与底层人民对话的组织")
        self.gi_("136","以及募集粮饷之类的")
        self.gi_("137","不过1925年孙中山先生逝世")
        self.gi_("138","委员长通过一系列纵横捭阖的手段")
        self.gi_("139","加之1927年北伐的胜利","使之声名极高")
        self.gi_("140","然后他随之发动了四一二事变","大肆屠杀共产党人")
        self.gi_("141","此时共产党的指导思想是陈独秀的","右倾投降机会主义")
        self.gi_("142","把希望寄托于委员长网开一面","放弃了共产党人的革命领导权")
        self.gi_("143","所以这个时期大量共产党人被屠杀")
        self.gi_("144","国共合作破裂","这是中国共产党的第一次重大危机")
        self.big_text("随后1927年8月1日")
        self.gi_("145","朱德，周恩来，叶挺，贺龙四位同志发动南昌起义")
        self.big_text("8月7日召开“八七会议”")
        self.gi_("146","确定了武装夺取政权的方针")


        tex[13] = self.flow_chart_start(LEFT*5+UP*2.5,"路线转变","大家注意这是中国共产党第一次重大路线的转弯")
        tex[14] = self.flow_chart_right(0,tex[13],"右倾投降","以前是陈独秀这种小资产阶级思想比较浓厚的路线",
                "他们不愿主动掌握政权去斗争")[1]
        tex[15] = self.flow_chart_right(0,tex[14],"武装反抗","而八七会议过后","中共正式确立了武装夺取政权的道路")[1]
        tex[16] = self.flow_chart_down(0,tex[15],"蒋乃骗子","而中共从高层也基本上看清了蒋介石就是一个精于权谋的骗子")[1]
        tex[17] = self.flow_chart_down(0,tex[16],"超脱个人的真理","在后续中共定立方针的时候",
        "都会考虑到国民党背信弃义的行为","以及中共高层开始意识到不以个人意志为转移的历史趋势")[1]
        tex[18] = self.flow_chart_start(LEFT*5,"四一二事变","比如这次四一二事变")
        tex[19] = self.flow_chart_right(1,tex[18],"蒋背信弃义","表面上是蒋介石的背信弃义")[1]
        tex[20] = self.flow_chart_right(0,tex[18],"必然结果","实质上民族矛盾与阶级矛盾所双重叠加的必然结果")[1]
        tex[21] = self.flow_chart_right(-1,tex[18],"中共损害地主买办","根本原因在于中共的共产主义损害了",
                "地主阶级与买办阶级的利益","当然还有背后的西方国家")[1]
        tex[22] = self.flow_chart_down(0,tex[21],"国民党政权的基石","而国民党政权的执政基石",
                "却是这些买办与地主")[1]
        tex[23] = self.flow_chart_down(0,tex[18],"继承封建王朝","这个政府对于过去封建王朝，买办阶级",
                "从本质上而言是继承的")[1]
        tex[24] = self.flow_chart_down(-1,tex[23],"军","表现在军事力量")[1]
        tex[25] = self.flow_chart_down(0,tex[23],"政","政治力量")[1]
        tex[26] = self.flow_chart_down(1,tex[23],"经","经济力量","三个方面的继承")[1]
        self.clear()
        self.gi_("147","用魔法打败魔法")
        self.two_fig("148","149","让军阀干掉军阀")
        self.gi_("150","这样建立的政府","到底还是军阀的政府")
        self.gi_("151","军阀的支撑力量是地主豪绅买办阶级")
        self.gi_("152","区区一个蒋介石","是无法调和这些具体而复杂的矛盾的")
        tex[27] = self.flow_chart_start(LEFT-LEFT,"蒋介石","这些本质上对立的矛盾")
        tex[28] = self.flow_chart_left(0,tex[27],"某些力量","蒋介石为了寻求某些力量的支持")[1]
        tex[29] = self.flow_chart_right(0,tex[27],"人民群众的对立面","就必然会走向人民群众的对立面")[1]
        tex[30] = self.flow_chart_down(0,tex[29],"中共的力量","而中共是由下而上的力量")[1]
        self.clear()
        self.gi_("153","典型的代表比如说毛泽东同志")
        self.gi_("154","教员在《中国社会的各阶级分析》")
        self.gi_("155","与《湖南农民运动考察报告》上","深刻分析了地主，农民，乡绅，资产阶级等等之间的")
        self.gi_("156","不可调和的只能斗争的矛盾")
        self.gi_("157","比如说农会这样的组织")
        self.gi_("158","他们是直接打击地主")
        self.gi_("159","给地主戴高帽子游乡等等","这些反映农民的利益")
        self.gi_("160","但是与国民党所依靠的地主豪绅","显然是矛盾的")
        self.gi_("161","所以对立是必然的趋势")
        self.gi_("162","八七会议后教员在湖南江西发动了秋收起义")
        self.gi_("163","起义失败后则来到了井冈山")
        self.gi_("164","在这里教员提出了“农村包围城市”的观点")
        self.gi_("165","这个观点有多牛逼呢？")
        self.gi_("166","你以现在的眼光来看","那就是几乎以一种预言家的姿态","替党的未来做出了十分精准的预言")
        self.gi_("167","当时全党根据苏联的革命经验以及马列的著作")
        self.gi_("168","基本上都认为要先从大城市、中心城市暴动")
        self.gi_("169","从而影响到全国")
        self.gi_("170","在那个教条主义盛行的时期","举个不恰当的例子")
        self.gi_("171","这个就相当于量子力学与相对论对牛顿力学造成的震憾一样")
        self.gi_("172","所以对于当时的中共而言","马克思主义中国化这种思想")
        self.gi_("173","无疑是振聋发聩的")
        self.gi_("174","当然在党内也就不受待见")
        self.gi_("175","当然还有一个原因就是","共产国际对中共的人事任免权力非常的大")
        self.gi_("176","在当时的环境中中共有种共产国际中国支部的感觉")
        self.gi_("177","这也是后来共产国际派人轻易的夺取了教员等人的领导权的原因")
        self.gi_("178","接下来就是蒋中正对井冈山地区的围剿了")
        self.gi_("179","前四次围剿中","由于是教员，朱德同志，林彪周志等人来领导")
        self.gi_("180","在中共灵活的游击战，运动战，歼灭战的指导思想下","委员长的进攻被粉碎了")
        self.gi_("181","并且根据地还在不断扩大")
        self.gi_("182","给大家解释一下这仗有多么难打吧")
        self.gi_("183","直接感觉就是农民拿着铁锹")
        self.gi_("184","去打别人的正规军的感觉")
        self.gi_("185","用游戏来举例的话","那大概就是拿两个辅助二打五")
        self.gi_("186","胜利简直就是神话")
        tex[31] = self.mind_start(LEFT*5,"方法","而我党采用的办法主要有以下几种")
        tex[32] = self.mind_node(1,tex[31],"团结群众","一是团结群众")[1]
        tex[33] = self.mind_node(0.5,tex[32],"组织赤卫队","一方面是组织赤卫队到地方拉人")[1]
        tex[34] = self.mind_node(-0.5,tex[32],"打土豪分地","另一方面则是打土豪分地拉拢群众")[1]
        tex[35] = self.mind_node(0,tex[31],"集中兵力","二是集中兵力")[1]
        tex[36] = self.mind_node(0,tex[35],"超过敌人","大多要超过敌人的兵力")[1]
        tex[37] = self.mind_node(-1,tex[31],"借助地形","三是借助地形")[1]
        tex[38] = self.mind_node(0,tex[37],"有利地形","找到对我们有利的地形")[1]
        tex[39] = self.mind_node(-2,tex[31],"运动战与歼灭战","四是运动战与歼灭战")[1]
        tex[40] = self.mind_node(0.5,tex[39],"一个月打一小时","运动到什么程度","基本上跑一个月打一小时这种感觉")[1]
        tex[41] = self.mind_node(-0.5,tex[39],"敌人犯错","什么时候打","要在敌人犯错的时候打")[1]
        self.clear()
        self.gi_("187","按教员的说法")
        self.gi_("188","任何敌人都会犯错")
        self.gi_("189","要诱导敌人犯错后再打")
        self.gi_("190","这种打法追求天时地利人和","集齐所有的有利因素才能打")
        self.gi_("191","就像你打游戏的时候","只有两个辅助那就二打一")
        self.gi_("192","不以消耗敌人的血线为目的","出手就要打死他")
        self.gi_("193","别人队形没有问题的")
        self.gi_("194","就要诱导别人的队形出现问题")
        self.gi_("195","要让别人内讧等等","大概就像这种感觉")
        self.gi_("196","对于当时弱小的红军而言","效果还是很好的")
        self.play(Transform(Text("一两千人",height=2),Text("十万人",height=2)),
                Write(Graphic("红军由一两千人发展到将近十万人")),
                run_time = len("红军由一两千人发展到将近十万人")*TIME_INTERVAL)
        self.clear()
        self.gi_("197","但是很可惜共产国际派来了王明等人","执行了左派激进的路线")
        self.gi_("198","在装备几乎有代差而且还得一打五的情况下","硬打打不过委员长啊")

class Party6(Graphic_Image):
    def construct(self):
        tex = [0 for i in range(50)]
        self.gi_("199","没办法只得突围转移根据地")
        self.gi_("200","但是可惜王明在撤退中犯了逃跑主义的错误")
        self.gi_("201","湘江战役后大概只剩下三万人左右")
        self.gi_("202","此时若是继续执行王明的路线","那么红军基本只有灭亡")
        self.gi_("203","关键时刻党内接受毛泽东同志的意见")
        self.gi_("204","往敌人力量薄弱的贵州方向去","到达遵义后开了遵义会议")
        self.gi_("205","会议过后红军的军事由","毛泽东，周恩来，王稼祥三人负责指挥","而中共也从此开始走向成熟")
        self.gi_("206","因为这是中共在与共产国际完全失联的情况下","独立做出的决定")
        self.gi_("207","从此政治，经济与军事方面","都不再依赖共产国际")
        self.gi_("208","直到1936年10月长征结束")
        self.gi_("209","接下来就是西安事变逼蒋抗日")
        a = self.flow_chart_start(LEFT*5,"毛泽东思想","至此毛泽东思想的框架已经形成")
        self.flow_chart_right(2,a[0],"独立自主","就是独立自主")
        self.flow_chart_right(0,a[0],"群众路线","群众路线")
        self.flow_chart_right(-2,a[0],"统一战线","统一战线")
        self.clear()
        self.gi_("211","后面就是卢沟桥事变","日本发动全面侵华战争了")
        self.big_text("但是限于时长问题")
        self.big_text("这些留在后面的视频叙述了")
        self.big_text("本视频最后我再给大家解释下")
        self.big_text("到此为止毛泽东思想有多牛逼吧")
        tex[0] = self.flow_chart_start(LEFT*5,"独立自主","先讲独立自主")
        tex[1] = self.flow_chart_right(2,tex[0][0],"救亡图存","大家知道自鸦片战争以来","诸多有志之士都开始了救亡图存的工作")
        tex[2] = self.flow_chart_right(1,tex[1][1],"洋务运动","先是洋务运动")
        tex[3] = self.flow_chart_right(0,tex[1][1],"维新变法","再是维新变法等等","然而他们都失败了")
        tex[4] = self.flow_chart_right(-1,tex[1][1],"自卑感","这个就导致了",
                "我们民族产生了一种强烈的自卑感","基本上西方国家说什么我们都信")
        tex[5] = self.flow_chart_right(1,tex[4][1],"政治","政治")
        tex[6] = self.flow_chart_right(0,tex[4][1],"经济","经济")
        tex[7] = self.flow_chart_right(-1,tex[4][1],"文化","文化上都是")
        group = self.group_(0,7,tex)
        self.play(ApplyMethod(group.shift,5*LEFT))
        self.wait(1)
        tex[8] = self.flow_chart_right(0,tex[7][1],"新文化运动","比较经典的一项运动就是新文化运动")
        tex[9] = self.flow_chart_down(0,tex[8][1],"全盘西化，否定自己","比较经典的一项运动就是新文化运动",
                "新文化运动的那种全面西化","彻底否定自己的态势","时至今日仍然有所影响")
        tex[10] = self.flow_chart_down(0,tex[9][1],"youtube","youtube上有许多这种这种",
                "中国啥都不行","西方国家啥都行的言论")
        group = self.group_(0,10,tex)
        self.play(ApplyMethod(group.shift,5*RIGHT))
        self.wait(1)
        tex[11] = self.flow_chart_right(-2,tex[0][0],"教员","所以教员告诉中国人民")
        tex[12] = self.flow_chart_right(1,tex[11][1],"独立自主自强不息","要相信自己凭借自己的能力发展下去")
        group = self.group_(0,12,tex)
        self.play(ApplyMethod(group.shift,LEFT*5+UP*2.5))
        self.wait(1)
        tex[13] = self.flow_chart_down(0,tex[12][1],"令人感到震憾","这种独立自主自强不息的精神","实在是令人感到震憾")
        tex[14] = self.flow_chart_down(0,tex[13][1],"教员正确","而历史证明","教员是正确")
        tex[15] = self.flow_chart_right(-3.5,tex[12][1],"掌握自己的命运","只有独立自主","中国人才能依靠自己的双手",
                "掌握自己的命运")
        tex[16] = self.flow_chart_right(-4.5,tex[12][1],"有底气","也只有独立自主","中国人的强大才是有底气的")
        self.clear()
        tex[17] = self.flow_chart_start(LEFT*5,"群众路线","再说群众路线")
        tex[18] = self.flow_chart_right(2,tex[17][1],"高层阶级","大家可能不知道","在那个时代",
                "中国的高层阶级对底层人民的态度")
        tex[19] = self.flow_chart_right(0,tex[18][1],"梁启超","比如梁启超说：民智低下，智慧不开",
                "总之底层人民都是“劳力者”的感觉","梁任公尚且是这种看法","其他人更是远远不及")
        group = self.group_(17,19,tex)
        self.play(ApplyMethod(group.shift,5*LEFT))
        self.wait(1)
        tex[20] = self.flow_chart_right(1,tex[19][1],"另一层意思","说出“民智低下”的另一层意思是")
        tex[21] = self.flow_chart_right(0.5,tex[20][1],"不是民","我不是民")
        tex[22] = self.flow_chart_right(-0.5,tex[20][1],"智力不低","我的智力不低下")
        tex[23] = self.flow_chart_right(-1,tex[19][1],"教育人民","所以他想要做的是","教育人民","把人民培养到他的那个智力")
        tex[24] = self.flow_chart_right(0.5,tex[23][1],"正确","他的想法当然是正确的")
        tex[25] = self.flow_chart_right(-0.5,tex[23][1],"难以实行","但是在那个时代","并没有实行的现实基础")
        tex[26] = self.flow_chart_down(0,tex[25][1],"权贵的时代","那个时代到底是权贵的时代","底层人民凭什么接受教育呢")
        group = self.group_(17,26,tex)
        self.play(ApplyMethod(group.shift,5*RIGHT))
        self.wait(1)
        tex[27] = self.flow_chart_right(-2,tex[17][1],"中国共产党","所以首先要做的还是")
        tex[28] = self.flow_chart_right(1,tex[27][1],"打倒地主","让当下的人民推翻当下的权贵")
        tex[29] = self.flow_chart_right(-0.8,tex[27][1],"接受教育","人民才有受到教育的权力","这是我们党的采用的方式")
        group = self.group_(17,29,tex)
        self.play(ApplyMethod(group.shift,3*LEFT))
        self.wait(1)
        tex[30] = self.flow_chart_right(1,tex[29][1],"人民决定历史","不管是哪个时代的人民","不管他们智力怎样",
                "人民这个群体才是决定历史方向的人")
        tex[31] = self.flow_chart_right(0,tex[29][1],"不可超脱","超脱于这个群体","则必然会导致失败")
        self.clear()
        tex[32] = self.flow_chart_start(LEFT*5,"统一战线","再说统一战线")
        tex[33] = self.flow_chart_right(2,tex[32][0],"原理","简单的来说")
        tex[34] = self.flow_chart_right(1,tex[33][1],"主要矛盾","就是先要确定一个主要矛盾")
        tex[35] = self.flow_chart_right(0,tex[34][1],"打倒小日本","比如打倒小日本")
        tex[36] = self.flow_chart_right(0,tex[33][1],"次要矛盾","然后与次要矛盾暂时和解")
        tex[37] = self.flow_chart_right(0,tex[36][1],"放下刀兵","那怕是蒋中正","也可暂时放下刀兵",
                "大家集中力量一致对外")
        tex[38] = self.flow_chart_right(0,tex[32][0],"本质","统一战线的本质")
        tex[39] = self.flow_chart_right(0.5,tex[38][1],"团结","就是团结所有可以团结的力量")
        tex[40] = self.flow_chart_right(-0.5,tex[38][1],"打击","去打击你的对手")
        tex[41] = self.flow_chart_right(-2,tex[32][1],"应用","这种思想","即使对于大家日常的工作与生活当中",
                "也是大有裨益")
        tex[42] = self.flow_chart_right(0,tex[41][1],"被讨厌","比如有人讨厌你")
        tex[43] = self.flow_chart_right(0,tex[42][1],"团结中立","那你就去团结那些中立的人")
        tex[44] = self.flow_chart_right(-1,tex[42][1],"瓦解敌人","先是对抗","然后在对抗中瓦解敌对势力",
                "变对手为朋友","国家之间的对抗如此")
        self.clear()
        self.big_text("好了本期视频到此结束")
        self.mind_start(LEFT-LEFT,"七月一号之前","后续部分今年之内会陆续做出","喜欢的朋友可以关注一下")
        self.clear()
        self.big_text("我是君子叶")
        self.big_text("我们下期再见")
        self.big_text("最后留一个小问题")
        self.big_text("在与日军装备有代差的情况下\n抗日战争为何可以取得胜利？")


class Party7(Graphic_Image):
    def construct(self):

        self.gi_("79","应该在圆明园遗址内给她","也立一个铜像")
        self.gi_("80","专门给人唾弃","耻辱，国之耻辱")
