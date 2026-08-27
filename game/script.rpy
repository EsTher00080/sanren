# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define player = Character(_("我"), color = "79575d")
define jth = Character(_("金泰亨·"), color = "79575d")
define yq = Character(_("Esthrr"), color = "79575d")
define rs = Character(_("入水"), color = "79575d")
define cy = Character(_("草原"), color = "79575d")
define xxw = Character(_("行星威"), color = "79575d")
define lf = Character(_("岚风"), color = "79575d")
define sx = Character(_("邪恶四小"), color = "79575d")

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
    scene bg dongkou
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
    "眼见一个蝰蛇战士前来炒股，蹲在了你攻击范围内的洞口。"
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
    "你不认识贤者的lb，只是你被原地控死没有乱跑才得意存活，你也大概get到这个技能能让你不受伤害。"

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

    show 
    

label continue1:
    player "……呃啊"

    # "猫魅族女性诗人"
    # "敖龙族女性贤者"
    # "维埃拉族男性骑士"



    return
