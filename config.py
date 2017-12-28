# coding=utf-8
# 这是为Google和中文维基(无缝整合)镜像配置的示例配置文件
#
# 使用方法:
#   1. 复制本文件到 zmirror 根目录(wsgi.py所在目录), 并重命名为 config.py
#   2. 修改 my_host_name 为你自己的域名
#
# 各项设置选项的详细介绍请看 config_default.py 中对应的部分
# 本配置文件假定你的服务器本身在墙外
# 如果服务器本身在墙内(或者在本地环境下测试, 请修改`Proxy Settings`中的设置
#
# 由于google搜索结果经常会出现中文维基, 所以顺便把它也加入了.
# google跟中文维基之间使用了本程序的镜像隔离功能, 可以保证中文维基站的正常使用
#
# 本配置文件试图还原出一个功能完整的google.
#   但是由于程序本身所限, 还是不能[完整]镜像过来整个[google站群]
#   在后续版本会不断增加可用的网站
#
# 以下google服务完全可用:
#   google网页搜索/学术/图片/新闻/图书/视频(搜索)/财经/APP搜索/翻译/网页快照/...
#   google搜索与中文维基百科无缝结合
# 以下服务部分可用:
#     gg地图(地图可看, 左边栏显示不正常)/G+(不能登录)
# 以下服务暂不可用(因为目前无法解决登录的问题):
#     所有需要登录的东西, docs之类的
#

# Github: https://github.com/aploium/zmirror

# ############## Local Domain Settings ##############
my_host_name = '127.0.0.1'
my_host_scheme = 'https://'
my_host_port = None  # None表示使用默认端口, 可以设置成非标准端口, 比如 81

# ############## Target Domain Settings ##############
target_domain = 'www.google.com'
target_scheme = 'https://'

# 这里面大部分域名都是通过 `enable_automatic_domains_whitelist` 自动采集的, 我只是把它们复制黏贴到了这里
# 实际镜像一个新的站时, 手动只需要添加很少的几个域名就可以了.
# 自动采集(如果开启的话)会不断告诉你新域名
external_domains = (
    '0-act.channel.facebook.com',
    '0-edge-chat.facebook.com',
    '1-act.channel.facebook.com',
    '1-edge-chat.facebook.com',
    '2-act.channel.facebook.com',
    '2-edge-chat.facebook.com',
    '3-act.channel.facebook.com',
    '3-edge-chat.facebook.com',
    '30.media.tumblr.com',
    '31.media.tumblr.com',
    '32.media.tumblr.com',
    '33.media.tumblr.com',
    '34.media.tumblr.com',
    '35.media.tumblr.com',
    '36.media.tumblr.com',
    '37.media.tumblr.com',
    '38.media.tumblr.com',
    '39.media.tumblr.com',
    '4-act.channel.facebook.com',
    '4-edge-chat.facebook.com',
    '40.media.tumblr.com',
    '41.media.tumblr.com',
    '42.media.tumblr.com',
    '43.media.tumblr.com',
    '44.media.tumblr.com',
    '45.media.tumblr.com',
    '46.media.tumblr.com',
    '47.media.tumblr.com',
    '48.media.tumblr.com',
    '49.media.tumblr.com',
    '5-act.channel.facebook.com',
    '5-edge-chat.facebook.com',
    '50.media.tumblr.com',
    '6-act.channel.facebook.com',
    '6-edge-chat.facebook.com',
    '65.media.tumblr.com',
    '66.media.tumblr.com',
    '67.media.tumblr.com',
    '90.media.tumblr.com',
    '91.media.tumblr.com',
    '92.media.tumblr.com',
    '93.media.tumblr.com',
    '94.media.tumblr.com',
    '95.media.tumblr.com',
    '96.media.tumblr.com',
    '97.media.tumblr.com',
    '98.media.tumblr.com',
    '99.media.tumblr.com',
    'about.twitter.com',
    'abs-0.twimg.com',
    'abs-1.twimg.com',
    'abs-2.twimg.com',
    'abs.twimg.com',
    'ac.dropboxstatic.com',
    'accounts.google.com',
    'accounts.google.com.hk',
    'accounts.gstatic.com',
    'accounts.youtube.com',
    'act.channel.facebook.com',
    'admin.brightcove.com',
    'ads.twitter.com',
    'afp.google.com',
    'ajax.googleapis.com',
    'ak.sail-horizon.com',
    'amp.twimg.com',
    'analytics.google.com',
    'analytics.twitter.com',
    'api-content-photos.dropbox.com',
    'api-content.dropbox.com',
    'api-d.dropbox.com',
    'api-notify.dropbox.com',
    'api-read.facebook.com',
    'api.adsymptotic.com',
    'api.demandbase.com',
    'api.dropbox.com',
    'api.dropboxapi.com',
    'api.facebook.com',
    'api.lytics.io',
    'api.tumblr.com',
    'api.twitter.com',
    'api.v.dropbox.com',
    'apis.google.com',
    'apps.facebook.com',
    'apps.google.com',
    'ar-ar.facebook.com',
    'assets.tumblr.com',
    'attachment.fbsbx.com',
    'attachments.facebook.com',
    'b-api.facebook.com',
    'b-graph.facebook.com',
    'b.6sc.co',
    'b.scorecardresearch.com',
    'b.static.ak.facebook.com',
    'b.static.ak.fbcdn.net',
    'b92.yahoo.co.jp',
    'bam.nr-data.net',
    'beta-chat-01-05-ash3.facebook.com',
    'bg-bg.facebook.com',
    'bigzipfiles.facebook.com',
    'block.dropbox.com',
    'block.v.dropbox.com',
    'blog.twitter.com',
    'blogs.dropbox.com',
    'bolt.dropbox.com',
    'books.google.com',
    'books.google.com.hk',
    'bot.talk.google.com',
    'brand.twitter.com',
    'brightcove01.brightcove.com',
    'bs-ba.facebook.com',
    'business.twitter.com',
    'c.brightcove.com',
    'ca-es.facebook.com',
    'calendar.google.com',
    'caps.twitter.com',
    'cards-dev.twitter.com',
    'cdn.static-economist.com',
    'cf.dropboxstatic.com',
    'cfl.dropboxstatic.com',
    'channel-ecmp-05-ash3.facebook.com',
    'channel-staging-ecmp-05-ash3.facebook.com',
    'channel-testing-ecmp-05-ash3.facebook.com',
    'chatenabled.mail.google.com',
    'check4.facebook.com',
    'check6.facebook.com',
    'chrome.google.com',
    'ci4.googleusercontent.com',
    'client-cf.dropbox.com',
    'client-channel.google.com',
    'client-lb.dropbox.com',
    'client-web.dropbox.com',
    'client.dropbox.com',
    'client.v.dropbox.com',
    'clients1.google.com',
    'clients2.google.com',
    'clients3.google.com',
    'clients4.google.com',
    'clients5.google.com',
    'clients6.google.com',
    'cloud.google.com',
    'code.facebook.com',
    'code.google.com',
    'connect.facebook.com',
    'connect.facebook.net',
    'consent-st.truste.com',
    'consent.truste.com',
    'contact.talk.google.com',
    'cookiex.ngd.yahoo.com',
    'creative.ak.fbcdn.net',
    'cs600.wac.alphacdn.net',
    'cse.google.com',
    'csi.gstatic.com',
    'cx.atdmt.com',
    'cynicallys.tumblr.com',
    'd.dropbox.com',
    'd.facebook.com',
    'd.v.dropbox.com',
    'd21j20wsoewvjq.cloudfront.net',
    'd6tizftlrpuof.cloudfront.net',
    'da-dk.facebook.com',
    'db.tt',
    'dbxlocal.dropboxstatic.com',
    'dc.ads.linkedin.com',
    'dcdevtzxo4bb0.cloudfront.net',
    'de-de.facebook.com',
    'debates.economist.com',
    'dev-hangoutssearch-pa-googleapis.sandbox.google.com',
    'dev.twitter.com',
    'developers.facebook.com',
    'developers.google.com',
    'dis.us.criteo.com',
    'dl-debug.dropbox.com',
    'dl-web.dropbox.com',
    'dl.dropbox.com',
    'dl.dropboxusercontent.com',
    'dl.google.com',
    'dnn506yrbagrg.cloudfront.net',
    'docs.google.com',
    'donate.twitter.com',
    'drive.google.com',
    'dropbox.com',
    'dropboxstatic.com',
    'edge-chat.facebook.com',
    'edge.quantserve.com',
    'el-gr.facebook.com',
    'encrypted-tbn0.gstatic.com',
    'encrypted-tbn1.gstatic.com',
    'encrypted-tbn2.gstatic.com',
    'encrypted-tbn3.gstatic.com',
    'encrypted.google.com',
    'engineering.twitter.com',
    'ent-a.xx.fbcdn.net',
    'ent-b.xx.fbcdn.net',
    'ent-c.xx.fbcdn.net',
    'ent-d.xx.fbcdn.net',
    'ent-e.xx.fbcdn.net',
    'error.facebook.com',
    'es-es.facebook.com',
    'es-la.facebook.com',
    'espresso.economist.com',
    'events.google.com',
    'execed.economist.com',
    'external-lax3-1.xx.fbcdn.net',
    'external.ak.fbcdn.net',
    'external.xx.fbcdn.net',
    'eydisrupters.films.economist.com',
    'fa-ir.facebook.com',
    'facebook.com',
    'families.google.com',
    'fb-s-c-a.akamaihd.net',
    'fb-s-d-a.akamaihd.net',
    'fbcdn-creative-a.akamaihd.net',
    'fbcdn-photos-a-a.akamaihd.net',
    'fbcdn-photos-a.akamaihd.net',
    'fbcdn-photos-b-a.akamaihd.net',
    'fbcdn-photos-c-a.akamaihd.net',
    'fbcdn-photos-d-a.akamaihd.net',
    'fbcdn-photos-e-a.akamaihd.net',
    'fbcdn-profile-a.akamaihd.net',
    'fbcdn-sphotos-a-a.akamaihd.net',
    'fbcdn-sphotos-a.akamaihd.net',
    'fbcdn-sphotos-b-a.akamaihd.net',
    'fbcdn-sphotos-c-a.akamaihd.net',
    'fbcdn-sphotos-d-a.akamaihd.net',
    'fbcdn-sphotos-e-a.akamaihd.net',
    'fbcdn-sphotos-f-a.akamaihd.net',
    'fbcdn-sphotos-g-a.akamaihd.net',
    'fbcdn-sphotos-h-a.akamaihd.net',
    'fbcdn-video-a-a.akamaihd.net',
    'fbcdn-video-b-a.akamaihd.net',
    'fbcdn-video-c-a.akamaihd.net',
    'fbcdn-video-d-a.akamaihd.net',
    'fbcdn-video-e-a.akamaihd.net',
    'fbcdn-video-f-a.akamaihd.net',
    'fbcdn-video-g-a.akamaihd.net',
    'fbcdn-video-h-a.akamaihd.net',
    'fbcdn-video-i-a.akamaihd.net',
    'fbcdn-video-j-a.akamaihd.net',
    'fbcdn-video-k-a.akamaihd.net',
    'fbcdn-video-l-a.akamaihd.net',
    'fbcdn-video-m-a.akamaihd.net',
    'fbcdn-video-n-a.akamaihd.net',
    'fbcdn-video-o-a.akamaihd.net',
    'fbcdn-video-p-a.akamaihd.net',
    'fbcdn-vthumb-a.akamaihd.net',
    'fbcdn.net',
    'fbexternal-a.akamaihd.net',
    'fbstatic-a.akamaihd.net',
    'feedburner.google.com',
    'fi-fi.facebook.com',
    'fi.google.com',
    'filetransferenabled.mail.google.com',
    'films.economist.com',
    'flash.dropboxstatic.com',
    'fonts.googleapis.com',
    'fonts.gstatic.com',
    'forums.dropbox.com',
    'fr-ca.facebook.com',
    'fr-fr.facebook.com',
    'friendconnectchat.google.com',
    'g.twimg.com',
    'g2.twimg.com',
    'get.google.com',
    'gg.google.com',
    'global1.cmdolb.com',
    'global2.cmdolb.com',
    'gmail.com',
    'gmail.google.com',
    'gmat.economist.com',
    'goku.brightcove.com',
    'googlemail.l.google.com',
    'goto.google.com',
    'gp3.googleusercontent.com',
    'graph.facebook.com',
    'gre.economist.com',
    'groupchat.google.com',
    'groups.google.com',
    'hangouts.google.com',
    'hca.twimg.com',
    'help.twitter.com',
    'hi-in.facebook.com',
    'horizon.economist.com',
    'hr-hr.facebook.com',
    'i.po.st',
    'ib.adnxs.com',
    'id-id.facebook.com',
    'id.google.com',
    'id.google.com.hk',
    'ie.talkgadget.google.com',
    'if-v6exp3-v4.metric.gstatic.com',
    'images.google.com',
    'images.google.com.hk',
    'imp2.ads.linkedin.com',
    'inbox.google.com',
    'infographics.economist.com',
    'inputtools.google.com',
    'instantarticles.fb.com',
    'investor.google.com',
    'inyour-slb-01-05-ash3.facebook.com',
    'ipv4.google.com',
    'isolated.mail.google.com',
    'it-it.facebook.com',
    'j.6sc.co',
    'ja-jp.facebook.com',
    'jobs.economist.com',
    'js.bizographics.com',
    'ko-kr.facebook.com',
    'l.facebook.com',
    'ldap.thefacebook.com',
    'lh1.googleusercontent.com',
    'lh2.googleusercontent.com',
    'lh3.googleusercontent.com',
    'lh4.googleusercontent.com',
    'lh5.googleusercontent.com',
    'lh6.googleusercontent.com',
    'link.brightcove.com',
    'linux.dropbox.com',
    'live.fb.com',
    'localhost.twitter.com',
    'log.getdropbox.com',
    'login.facebook.com',
    'login.wikimedia.org',
    'ls.srvcs.tumblr.com',
    'm.android.com',
    'm.dropbox.com',
    'm.facebook.com',
    'm.gmail.com',
    'm.google.com',
    'm.googlemail.com',
    'ma-0.twimg.com',
    'ma-1.twimg.com',
    'ma-2.twimg.com',
    'ma.twimg.com',
    'mab.chartbeat.com',
    'mail-settings.google.com',
    'mail.google.com',
    'managingbias.fb.com',
    'manifest.googlevideo.com',
    'maps-api-ssl.google.com',
    'maps.google.com',
    'maps.google.com.hk',
    'maps.googleapis.com',
    'maps.gstatic.com',
    'marketing.dropbox.com',
    'marketingsolutions.economist.com',
    'media-llnw.licdn.com',
    'media.economist.com',
    'media.tumblr.com',
    'media.twitter.com',
    'message-facebook.com',
    'messengerplatform.fb.com',
    'meta.wikimedia.org',
    'metrics.brightcove.com',
    'mk-mk.facebook.com',
    'mobile.twitter.com',
    'mpp.mxptint.net',
    'mqtt.facebook.com',
    'ms-my.facebook.com',
    'muvc.google.com',
    'mx.tumblr.com',
    'myaccount.google.com',
    'myaccount.google.com.hk',
    'myphonenumbers-pa.googleapis.com',
    'netdna.bootstrapcdn.com',
    'news.google.com',
    'news.google.com.hk',
    'nonprofits.fb.com',
    'notifications.google.com',
    'notify.dropbox.com',
    'o.twimg.com',
    'onetoday.google.com',
    'orcart.facebook.com',
    'origincache-ai-01-05-ash3.fbcdn.net',
    'origincache-starfacebook-ai-01-05-ash3.facebook.com',
    'p.po.st',
    'partner.googleadservices.com',
    'payments.google.com',
    'pbs.twimg.com',
    'people-pa.clients6.google.com',
    'photos-1.dropbox.com',
    'photos-2.dropbox.com',
    'photos-3.dropbox.com',
    'photos-4.dropbox.com',
    'photos-5.dropbox.com',
    'photos-6.dropbox.com',
    'photos-a.ak.fbcdn.net',
    'photos-b.ak.fbcdn.net',
    'photos-c.ak.fbcdn.net',
    'photos-d.ak.fbcdn.net',
    'photos-e.ak.fbcdn.net',
    'photos-f.ak.fbcdn.net',
    'photos-g.ak.fbcdn.net',
    'photos-h.ak.fbcdn.net',
    'photos-thumb.dropbox.com',
    'photos-thumb.x.dropbox.com',
    'photos.dropbox.com',
    'photos.google.com',
    'pic.twitter.com',
    'picasa.google.com',
    'picasaweb.google.com',
    'ping.chartbeat.net',
    'pixel.facebook.com',
    'pixel.fetchback.com',
    'pixel.quantserve.com',
    'pl-pl.facebook.com',
    'platform.linkedin.com',
    'platform.twitter.com',
    'play.google.com',
    'players.brightcove.net',
    'plus.google.com',
    'plus.googleapis.com',
    'plus.sandbox.google.com',
    'po.st',
    'preprod.hangouts.sandbox.google.com',
    'privacy.google.com',
    'productforums.google.com',
    'profile.ak.facebook.com',
    'profile.ak.fbcdn.net',
    'profiles.google.com',
    'prom.corp.google.com',
    'pt-br.facebook.com',
    'pt-pt.facebook.com',
    'public.talk.google.com',
    'publish.twitter.com',
    'px.srvcs.tumblr.com',
    'quickread.twitter.com',
    'radio.economist.com',
    'research.google.com',
    'rightsmanager.fb.com',
    'ro-ro.facebook.com',
    's-external.ak.fbcdn.net',
    's-static.ak.facebook.com',
    's-static.ak.fbcdn.net',
    's-static.facebook.com',
    's-v6exp1-ds.metric.gstatic.com',
    's.po.st',
    's.yimg.com',
    's3.amazonaws.com',
    'sadmin.brightcove.com',
    'sb.scorecardresearch.com',
    'schemas.google.com',
    'scontent-a-lax.xx.fbcdn.net',
    'scontent-a-sin.xx.fbcdn.net',
    'scontent-a.xx.fbcdn.net',
    'scontent-b-lax.xx.fbcdn.net',
    'scontent-b-sin.xx.fbcdn.net',
    'scontent-b.xx.fbcdn.net',
    'scontent-c.xx.fbcdn.net',
    'scontent-d.xx.fbcdn.net',
    'scontent-e.xx.fbcdn.net',
    'scontent-lax3-1.xx.fbcdn.net',
    'scontent-mxp.xx.fbcdn.net',
    'scontent.xx.fbcdn.net',
    'script.google.com',
    'secure-profile.facebook.com',
    'secure.adnxs.com',
    'secure.assets.tumblr.com',
    'secure.facebook.com',
    'secure.quantserve.com',
    'secure.static.tumblr.com',
    'security.google.com',
    'service.maxymiser.net',
    'shop.economist.com',
    'sites.google.com',
    'sjs.bizographics.com',
    'sl-si.facebook.com',
    'snap.licdn.com',
    'snapengage.dropbox.com',
    'sp.analytics.yahoo.com',
    'sr-rs.facebook.com',
    'ssl.facebook.com',
    'ssl.gstatic.com',
    'sstats.economist.com',
    'staging.talkgadget.google.com',
    'stags.bluekai.com',
    'star.c10r.facebook.com',
    'star.facebook.com',
    'static.ak.facebook.com',
    'static.ak.fbcdn.net',
    'static.chartbeat.com',
    'static.criteo.net',
    'static.thefacebook.com',
    'static.xx.fbcdn.net',
    'staticxx.facebook.com',
    'stats.economist.com',
    'stats.g.doubleclick.net',
    'status.dropbox.com',
    'status.twitter.com',
    'storage.googleapis.com',
    'store.google.com',
    'stun.l.google.com',
    'stun1.l.google.com',
    'stun2.l.google.com',
    'stun3.l.google.com',
    'stun4.l.google.com',
    'subscriptions.economist.com',
    'success.economist.com',
    'support.google.com',
    'support.twitter.com',
    'syndication.twitter.com',
    't.co',
    't.lv.twimg.com',
    't.myvisualiq.net',
    't0.gstatic.com',
    't1.gstatic.com',
    't2.gstatic.com',
    't3.gstatic.com',
    'tags.bkrtx.com',
    'tags.bluekai.com',
    'tags.tiqcdn.com',
    'tailfeather.twimg.com',
    'talkgadget.google.com',
    'tdapi-staging.atla.twitter.com',
    'tdapi-staging.smf1.twitter.com',
    'techprep.fb.com',
    'th-th.facebook.com',
    'threatexchange.fb.com',
    'ton.twimg.com',
    'ton.twitter.com',
    'tools.google.com',
    'touch.facebook.com',
    'translate.google.com',
    'translate.google.com.hk',
    'translate.googleusercontent.com',
    'tt.mbww.com',
    'tumblr.co',
    'tumblr.com',
    'tweetdeck-devel.atla.twitter.com',
    'tweetdeck-devel.smf1.twitter.com',
    'tweetdeck.localhost.twitter.com',
    'tweetdeck.twitter.com',
    'twitter.com',
    'uds.ak.o.brightcove.com',
    'upload.facebook.com',
    'upload.twitter.com',
    'upload.wikipedia.org',
    'vi-vn.facebook.com',
    'video-lax3-1.xx.fbcdn.net',
    'video.google.com',
    'video.google.com.hk',
    'video.twimg.com',
    'video.xx.fbcdn.net',
    'vpn.tfbnw.net',
    'vt.tumblr.com',
    'vthumb.ak.fbcdn.net',
    'vupload.facebook.com',
    'vupload2.vvv.facebook.com',
    'w.usabilla.com',
    'wallet.google.com',
    'webcache.googleusercontent.com',
    'webservices.sub2tech.com',
    'work.fb.com',
    'worldif.economist.com',
    'www-onepick-opensocial.googleusercontent.com',
    'www.dropboxstatic.com',
    'www.facebook.com',
    'www.gmail.com',
    'www.google-analytics.com',
    'www.google.com',
    'www.googleapis.com',
    'www.googletagmanager.com',
    'www.googletagservices.com',
    'www.gstatic.com',
    'www.linkedin.com',
    'www.thepiratebay.org',
    'www.tumblr.com',
    'www.v.dropbox.com',
    'youtube.googleapis.com',
    'zh-cn.facebook.com',
    'zh-tw.facebook.com',
    'zh.m.wikipedia.org',
    'zh.wikipedia.org',
)

# 强制所有Google站点使用HTTPS
force_https_domains = 'ALL'

# 自动动态添加域名
enable_automatic_domains_whitelist = True
domains_whitelist_auto_add_glob_list = (
    '*.akamaihd.net', '*.alphacdn.net', '*.bizographics.com', '*.bluekai.com', 
    '*.brightcove.com', '*.cdnetworks.net', '*.cdninstagram.com', '*.cedexis-radar.net', 
    '*.chartbeat.com', '*.chartbeat.net', '*.cloudfront.net', '*.doubleclick.net', 
    '*.dropbox.com', '*.dropboxstatic.com', '*.economist.com', '*.facebook.com', 
    '*.facebook.net', '*.fb.com', '*.fbcdn.net', '*.google.com', '*.google.com.hk', 
    '*.googleapis.com', '*.googleusercontent.com', '*.gstatic.com', '*.instagram.com', 
    '*.licdn.com', '*.quantserve.com', '*.scorecardresearch.com', '*.static-economist.com', 
    '*.thepiratebay.org', '*.tiqcdn.com', '*.tumblr.com', '*.twimg.com', '*.twitter.com',
)

# ############## Proxy Settings ##############
# 如果你在墙内使用本配置文件, 请指定一个墙外的http代理
is_use_proxy = False
# 代理的格式及SOCKS代理, 请看 http://docs.python-requests.org/en/latest/user/advanced/#proxies
requests_proxies = dict(
    http='http://127.0.0.1:8123',
    https='https://127.0.0.1:8123',
)

# ############## Sites Isolation ##############
enable_individual_sites_isolation = True

# 镜像隔离, 用于支持Google和维基共存
isolated_domains = {'zh.wikipedia.org', 'zh.m.wikipedia.org'}

# ############## URL Custom Redirect ##############
url_custom_redirect_enable = True
url_custom_redirect_list = {
    # 这是一个方便的设置, 如果你访问 /wiki ,程序会自动重定向到后面这个长长的wiki首页
    '/wiki': '/extdomains/https-zh.wikipedia.org/',
    # 这是gmail
    '/gmail': '/extdomains/mail.google.com/mail/u/0/h/girbaeneuj90/',
}

# ############# Additional Functions #############
# 移除google搜索结果页面的url跳转
#   原理是往页面中插入一下面这段js
# js来自: http://userscripts-mirror.org/scripts/review/117942
custom_inject_content = {
    "head_first": [
        {
            "content": r"""<script>
function checksearch(){
   var list = document.getElementById('ires');
   if(list){
       document.removeEventListener('DOMNodeInserted',checksearch,false);
       document.addEventListener('DOMNodeInserted',clear,false)
   }
};

function clear(){
   var i; var items = document.querySelectorAll('a[onmousedown]');
   for(i =0;i<items.length;i++){
       items[i].removeAttribute('onmousedown');
   }
};
document.addEventListener('DOMNodeInserted',checksearch,false)
</script>""",
            "url_regex": r"^www\.google(?:\.[a-z]{2,3}){1,2}",
        },
    ]
}
