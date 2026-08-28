# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define player = Character(_("我"), color = "79575d")
define jth = Character(_("金泰亨·（吟游诗人）"), color = "79575d")
define yq = Character(_("Esthrr（贤者）"), color = "79575d")
define rs = Character(_("入水（武士）"), color = "79575d")
define cy = Character(_("草原（骑士）"), color = "79575d")
define xxw = Character(_("行星威（武士）"), color = "79575d")
define lf = Character(_("岚风（蝰蛇剑士）"), color = "79575d")
define sx = Character(_("邪恶四小"), color = "79575d")
define ncg = Character(_("耐草哥(武僧)"), color = "79575d")



# 正常状态（全彩）
transform normal_sprite:
    matrixcolor IdentityMatrix()
    ease 0.3 alpha 1.0  # 恢复全亮

# 暗化/阴影状态（调暗，比如降低亮度或染上深灰色）
transform dim_sprite:
    # TintMatrix 可以把立绘整体染成暗灰色，模拟内心的阴影或旁观感
    matrixcolor TintMatrix("#888888") 
    # 或者用 BrightnessMatrix(-0.3) 纯粹降低亮度
    # matrixcolor BrightnessMatrix(-0.3)
    ease 0.3 alpha 0.8  # 顺便微微降低一点透明度

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg haidu
    play music "audio/haidu.mp3" fadein 1.0
    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    # These display lines of dialogue.

    "——利姆萨·罗敏萨下层甲板"
    "豆豆柴红茶川服务器，熟悉的海都一如往常般热闹。"
    "虽然不必陆行鸟大都市一般的喧嚣，但依旧有不少人在此处挂机、闲聊、购物。"
    "只是此刻，烦闷的内心让你无暇顾及身旁大吵大闹的一群拉拉肥。"
    
    player "这都排多久了……{w=0.3}还不开闸？"

    "没错，十分钟前你便提交了\"每日挑战：纷争前线\"的任务申请。"
    "自从新版本更新后，开闸时间一推再推，原本八点半就能开闸的豆豆柴，此刻九点多都没排到第一闸。"
    "更何况今天是最受欢迎的地图尘封密岩.作为还没缝完通行证的散人莫古仔的你，感到深深的无力。"

    player "人都去牢新月岛了吗？海都挂机的点点小鼠标助力开闸好不好。"
    "此刻的你真有点想发橙字让这群看上去就很会打pvp的潮人进进闸"
    "喊话的文字已经在对话框中敲好，亟待发送。"
    
    menu choice_kaizha:
        player "要不要发出去呢？"
        "发":
            jump kaizha1
        "还是算了":
            jump kaizha2
          
label kaizha1:
    
    player "\"排排战场喵，排排战场谢谢喵!\""
    "醒目的橙字侵入了每个人的对话框，但是许久后都没人回应。"
    "你的喊话没有激起任何波澜，大家仍旧做着自己的事。"
    "这让你感到有些尴尬，赶紧蹦跳着跑到了离人群远一点的地方。"
    "不过……"
    "你好像隐隐看到，有几个id前冒出了任务申请的标记。"
    
    jump tiaole
    
label kaizha2:
    "犹豫片刻后，你还是删除了对话框的文字。"
    player "算了……要是没人鸟我就太尴尬了，再等等吧总会跳的。"

    "无聊的你打开了招募板。玩家对战的栏目里赫然有一个写着一串等于号的招募。"
    "显然这是一队四小,{w=0.2}你默默记下了招募人的id。"
    
    jump tiaole

label tiaole:
    "——叮！"
    "像是感受到了你的心愿，任务确认的音效应景地响起。你急忙点下了确认键，迫不及待地进闸了。"
    
    jump kaiju

label kaiju:
    scene bg cfmy_home
    with fade
    play music "audio/cfmy_home.mp3" fadein 1.0 fadeout 1.0

    "屏幕一黑后紧接着亮起，你绝望地看到自己出生在了洞家。"
    player "完蛋……{w=0.5}待会又要被夹了。"

    "狗区的指挥宏哥本就不多，战意系统改版后，闸里四小群魔乱舞，更是鲜少有人愿意发宏。"
    "你简单看了一下队友的阵容和id，果不其然都是散人。"
    player "哎，这下要被四小当猪杀了。"
    "面对看上去毫无胜算的阵容，你仔细思考着职业的选择。"

    menu choice_zhiye:
        player "选什么好呢？"
        "人见人嫌的武士":
            jump wushi
        "人见人爱的诗人":
            jump shiren
        "人山人海的骑士":
            jump qishi
        "人畜无害的召唤":
            jump zhaohuan

label wushi:
    player "要不试试盘子？我还没拿到主宰呢。"
    "你想起了之前玩盘子2-5-9的战绩，\"一换一不亏\",你连一换一都做不到"
    player "呃……还是算了吧，我不擅长这个。"

    jump choice_zhiye

label shiren:
    "你想起前段时间在小*书刷到某博主用诗人在大草原狂k的视频，跃跃欲试。"
    player "我要不要也试试这个！"
    "你激动地切换成诗人，然而身上的幻化散件全部乱套，完全不搭调的猎奇穿搭赫然展现在你身上。"
    "四周围上来了一些奇怪的目光，你的脸上瞬间姹紫嫣红。"
    player "……沟槽的jtzs。"
    "本能的反应让你赶紧切掉了这个职业，还是换一个吧。"

    jump choice_zhiye

label qishi:
    player "偶尔玩玩前排吧……{w=0.5}比如有无敌的骑士？"
    "你的鼠标悬停在骑士套装的按键上许久。"
    player "队友几乎全是后排，我一个人前压不久白白被卖！"
    "你的骑士玩的本就不熟练，不知道有多少次无敌的动画还没播完，血条就见了底，让你白白浪费了LB。"
    "更不用说保护队友了，身上如果出现舞伴图标，你会像期末考试的学生一样紧张无比。"
    player "果然我还是只想按摩大脑，这种职业太不适合我了。"

    jump choice_zhiye

label zhaohuan:
    player "果然，莫古仔就要配烂远啊！"
    "你选择了熟悉的召唤师职业，决定让耀祖巴哈帮你多叼几个头回来。"
    jump duiyou

label duiyou:
    "选好了心仪的职业，你右键翻着小队列表的铭牌，等待准备倒数结束。"
    player "果然pvp的铭牌都味冲。"
    "你打开了一个猫男的铭牌，感慨道。"
    "队伍里几个看上去有些眼熟的人引起了你的注意。"
    player "……唉？{w=0.3}这个好像是小*书上那个……"
    
    show cy black at center
    "你注意到队伍里的粉发兔男骑士，此刻他正躺在魔法飞床上，看上去十分悠闲。"
    "看上去和你前几天在社媒上刷到过的博主有点像，不过你不敢确定。"
    hide cy 

    show yq black at left
    show jth black at right
    "队伍里有个贤者频繁切换着关心的对象，你选中二人。是一个龙娘和一个猫娘，看样子她们是组排。"
    hide yq
    hide jth

    show rs black at center 
    "{color=#79575d}维埃拉族女性武士{/color}" "……"
    "角落里一位沉默的兔娘，身上散发着强大的气息，让你不忍侧目。"
    hide rs



    player "总感觉这些人不是一般的莫古仔……"
    "直觉告诉你，这群散人中有不输四小和宏哥的强大存在"
    "不容你想太多，围栏已经放下，所有焦躁难耐的散人一涌而出。"

    stop music
    play music "audio/cfmy_chufa.mp3"
    jump diyibo

label diyibo:
    scene bg cfmy_dongkou
    with dissolve
    play music "audio/cfmy_fight.mp3" fadein 1.0
    
    "三家已然来到了海边的B2，此时上下家正激烈地战斗，你和队友一起逮着人就吐吐口水，没有人敢往前顶。"
    
    play sound "audio/skills/fengquan.mp3"
    play sound "audio/skills/fengquan.mp3"    
    play sound "audio/skills/fengquan.mp3"
    pause 1.5
    player "* * * ，让我吐个风圈行不行！"
    "每当有敌人出现在可及的距离，你便迫不及待地摁下螺旋气流的技能，只是读条还没完便丢失了目标，让你逐渐暴躁。"
    show npc at center
    player "!!!"
    "眼见一个蝰蛇剑士前来炒股，蹲在了你攻击范围内的洞口。"
    player "好机会！"
    "蛇鳞术期间攻击他显然是犯了大忌，不过你只是一个莫古仔，待会蝰蛇吸满汤汁砍死一片你也可以推脱说队友也干了。"

    play sound "audio/skills/fengquan.mp3"
    player "终于扔出去了……"
    "就在你因为扔掉了技能心情舒畅之时，背后压过来一片不祥的阴影。"
    hide npc

    play sound "audio/hong/jiaji.mp3"
    show jintaiheng shout
    "{color=#79575d}猫魅族女性诗人{/color}" "小心夹击！"
    hide jintaiheng shout

    "刚才还在争斗B2的下家，神不知鬼不觉地从另一侧洞口绕了进来。你顿感不妙，急忙往回走，却还是为时已晚。"
    
    play sound "audio/skills/qianchongbu.mp3"
    play sound "audio/skills/dk.mp3"
    play sound "audio/skills/longqi.mp3"

    player "完了……"
    "不会摁净化的你被腐秽大地狠狠吸入，舞者的魅惑让你动弹不得。眼见着对面龙骑的大腚就要落下，你闭上了双目体面地迎接死亡。"
    play sound "audio/skills/lb.mp3"
    
    menu choice_save1:
        "你不可思议地睁开了眼，惊讶地发现自己活了下来，救下你的是？"
        "敖龙族女性贤者":
            jump yq_save1
        "维埃拉族男性骑士":
            jump caoyuan_save1

label yq_save1:
    show yq shout 
    yq "快躲进贤圈里！"
    play sound "audio/skills/lb.mp3"

    "中庸之道的特效几乎完美与腐秽大地重合，龙骑应声落下，而你的血条却纹丝不动。"
    
    show yq sweat
    yq "还好手速快……诶！还烫死几个。"
    "你不认识贤者的LB，只是你被原地控死没有乱跑才得意存活，你也大概get到这个技能能让你不受伤害。"

    player "啊……谢谢你救了我。"
    show yq smile
    yq "出去记得给我点赞哦，么么啾~"

    show yq smile at dim_sprite
    "救命之恩，点个小赞确实没什么，只是你多半会忘记这回事，马上退出开下一把。"
    
    hide yq
    jump continue1

label caoyuan_save1:
    "此刻，身上赫然出现了一条白色的细线，另一端连着的正是同队的骑士"
    play sound "audio/skills/lb.mp3"

    show cy normal
    cy "保护你了，别担心。"
    show cy normal at dim_sprite
    "敌方倾倒而来的伤害全部通过连接传到了骑士身上，无法对开着无敌的他造成分毫的擦伤"
    player "谢谢骑士！"
    show cy smile at normal_sprite
    "兔男回敬了一个微笑"
    hide cy 

    jump continue1

label continue1:
    play sound "audio/skills/longpao.mp3"
    
    "救下一条命的技能结束了他的使命，对面的龙骑却气急败坏地对你继续丢着小技能。"
    player "……呃啊！"

    show jth normal 
    show skills guangyinshen
    jth "给你净化了，快往回走。"
    hide skills guangyinshen

    player "……谢谢……"
    hide jth
    "身上被施加光阴神祝福的你急忙挂上疾跑往回撤，总算让吃烂头的龙骑心有不甘地走开了。"

    jump dierbo

label dierbo:
    scene bg cfmy_a2

    "……"
    "刚刚的风波平息后不久，新一波点位已经刷新。你深知自己最大的贡献应该是摸点，于是朝着A2的方向走去。"
    player "死腿快跑，我要刷尘秘守护者。"

    "其他队友果然还是晚你一步，你率先到达点位，蹲下摸了起来。"

    show xxw normal
    play sound "audio/skills/panzi.mp3"

    player "什么东西断我点！"
    show xxw smile
    player "讨厌的盘子……"
    "来者是敌方的武士，对方并没有理会你的吐槽，可一旦你蹲下摸点，她便拿太刀戳你两下。你一下子被搞炸毛了。"
    player "阿西吧，我和你拼了——！"
    with vpunch

    show xxw normal at dim_sprite
    play sound "audio/skills/zhaohuan.mp3"
    play sound "audio/skills/huixie.mp3"

    "吐了半天口水，武士一口热水就回了上来。你甚至有点想把巴哈丢出来了，可是你只是一个莫古仔，舍不得你宝贵的LB。"
    
    menu choice_modian:
        player "再这样下去不是办法……到底要不要摸这个点？"
        
        "就算是为了尊严，一定要把A2拿下！":
            jump die_1

        "还是别继续纠缠了。":
            jump continue2

label die_1:
    player "臭盘子，我队友马上来了，到时候你想走都走不了！"
    "你卯足了劲，在点位上放下了巴哈，企图赶走面前的敌方野王。为了加大剂量，你补充了一发幻影弹。"
    show xxw smile at normal_sprite
    play sound "audio/skills/ditian.mp3"
    "盘子露出了诡异的笑容。"
    play sound "audio/skills/lb.mp3"
    show xxw smile at dim_sprite
    with hpunch
    # 1. 隐藏常规对话框
    window hide

    # 2. 渐变切换到全黑背景
    scene expression "#000000" with dissolve

    # 3. 开启文本窗口，输出结局描述文字
    window show
    
    "这次没有队友的帮助，你在刀光间成为了可怜的4战意。"
    "【BAD END：侍好吃吗】"

    # 4. 文字播完后稍作停留，然后退出
    pause 2.0
    $ renpy.quit()


label continue2:

    show xxw normal at normal_sprite
    player "算了算了，你赢了，我不摸这个点了。"
    hide xxw

    scene bg cfmy_d1_1

    "此时队友正待在D1这个不妙的位置，你前去与他们汇合，然而敌方的大团也已经到达了A2。莫古仔队友看到人就扔下点准备跑路。"

    "聪明的队友竟然选择从D1的窄口离开，不会走路的你坚定跟着大部队走就是对的，也凑了上去。"

    play sound "audio/skills/qianchongbu.mp3"

    player "完了。"

    show npc at center
    sx "这群 * * 蘑菇仔路都不会走，看我一个飞天大夹击全给你吃了！"
    show npc:
        left
        dim_sprite

    show ncg normal at right
    
    play sound "audio/skills/lb.mp3"
    
    show npc:
        left
        normal_sprite
    sx "骑士被踹了……！没保上……"

    "四小显然没料到屁股后面会突然冒出来一个武僧，舞者已经前冲步进场，没有保护的脆皮被队友恐惧的乱火送回了家。"
    hide npc
    hide ncg

    show ncg normal at center
    player "好拆！"
    show ncg smile at center
    ncg "（ ac 伸了伸拳头想要对碰一下）"

    show npc at center
    "舞者和骑士双双失利，只剩已经跳斩入场的 dk 与上天的龙骑二人，你撑开蓝盾。"

    show rs angry at center
    rs "四小……"
    play sound "audio/skills/ditian.mp3"
    rs "你们刚刚，有在打老三吧。"
    
    show npc at center
    with vpunch
    "4秒结束，龙骑落在了同样来不及停手的dk留下的腐秽大地中，而二人身上都出现了令人心惊肉跳的蓝紫色buff。"
    show rs angry at center
    play sound "audio/skills/lb.mp3"
    pause 1.0
    
    show npc at center
    sx "有斩钅……"
    "薄盾抵不住队友不断骚扰的小火，血条赤裸地展现出来，又在刹那间归了零。"
    hide npc

    show rs smile at center
    rs "安心吧，都解决了。"
    "兔娘纳刀，朝你的方向偏头一笑。"
    player "好帅气……盘子也能这么美丽吗。"
    hide rs 
    

    menu choice_tiaoshi:
        "你为队友精妙的配合感到高兴，想通过手舞足蹈表示这份心情。"
        "蹦蹦跳跳":
            jump tiaoshi 
        "做情感动作":
            jump tushi
        "什么都不做":
            jump wushifasheng

label tiaoshi:
    "你高兴地原地蹦跳了好几下，欢呼着小小的胜利。队友看向你的眼神却变得诡异起来，纷纷扭头不再与你互动。"
    "你感到奇怪，后知后觉地发现刚刚所在位置的脚下正是四小的尸体。"

    scene cfmy_d1_2
    "战斗仍旧进行着，只是失去了魔王护的你血量频频告急。"
    "躲在后排打药的时候，你似乎远远看到有四个头上带标记的武僧朝你走来。"
    play sound "audio/skills/lb.mp3"
    play sound "audio/skills/lb.mp3"
    play sound "audio/skills/lb.mp3"
    play sound "audio/skills/lb.mp3"
    pause 1.5
    window hide

    scene expression "#000000" with dissolve

    window show
    "刚刚的四小被你跳尸，气急败坏地切了武僧，你在四个大臭脚的轮番攻击下变成了肉泥。这次没有人保护你。"
    "【BAD END：招募板见】"

    pause 2.0
    $ renpy.quit()

label tushi:
    "你打开情感动作列表，想要做一个振奋人心的动作，却不小心误触了陆行鸟笔。"
    "情感动作播报没有关闭，所有人左下角都跳出了你的消息。你赶忙想用其他动作盖过去，着急忙慌之下居然又多摁了几遍。"
    "队友看向你的眼神却变得诡异起来，纷纷扭头不再与你互动。此刻你所在位置的脚下正是四小的尸体。"

    scene cfmy_d1_2
    "战斗仍旧进行着，只是失去了魔王护的你血量频频告急。躲在后排打药的时候，你似乎远远看到有四个头上带标记的武僧朝你走来。"
    play sound "audio/skills/lb.mp3"
    play sound "audio/skills/lb.mp3"
    play sound "audio/skills/lb.mp3"
    play sound "audio/skills/lb.mp3"
    pause 1.5
    window hide

    scene expression "#000000" with dissolve

    window show
    "刚刚的四小被你涂尸，气急败坏地切了武僧，你在四个大臭脚的轮番攻击下变成了肉泥。这次没有人保护你。"
    "【BAD END：这里不是喷喷】"

    pause 2.0
    $ renpy.quit()

label wushifasheng:
    player "打战场呢严肃点，别整这些花里胡哨的了，活下来就是最大的报答。"
    "你收起了整活的念头，继续加入战斗。"
    jump continue2_2

label continue2_2:
    scene cfmy_d1_2

    "D1方向还有不少残血的敌人，你终于舍得扔出宝贵的LB，却全给队友垫伤害了，你气急败坏地补了一个火神冲。"
    play sound "audio/skills/ditian.mp3"
    show xxw smile at center
    pause 0.5
    "蓝紫色的标记此刻出现在了你和队友的身上。"
    player "有斩钅……"
    play sound "audio/skills/lb.mp3"
    pause 0.5
    "D1窄口提供了天然的聚敌优势，斩铁剑一道直线穿过，地上出现了整整五具尸体。"
    "其中又没有你……你又被队友捞了。"
    show yq normal at left
    show ncg normal at center
    show cy normal at right 
    player "谢谢呃，贤者的输血、武僧的轻身步法、骑士的保护，还有我自己的宝宝盾。"
    "你有一种被所有人当作重点关注对象的感觉。当然你清楚只是因为你是队里最菜的。"
    hide yq
    hide ncg
    hide cy 
    show xxw sweat at center
    xxw "……这盾比我命都厚。"
    hide xxw
    "你有些惭愧，是自己的莽撞让队友不得不在自己身上浪费资源。你沉默地回到了家门口的D2，不去送就是最大的贡献了。"




    return
