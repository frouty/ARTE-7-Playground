# -*- coding: utf-8 -*-
import json
false=False
true=True
dico = {
        "videoSearchParams":{
                            "detailLevel":"L1",
                            "lang":"F",
                            "offset":0,
                            "searchOperator":"OR",
                            "order":"AIRDATE_DESC",
                            "videoId":["055178-000_PLUS7-F"],
                            "videoFormat":"ALL",
                            "videoQuality":"ALL",
                            "mobileAvailable":false,
                            "tvAvailable":false,
                            "pcAvailable":true,
                            "prereleased":0,
                            "firstVideoId":"055178-000_PLUS7-F",
                            "searchFields":["videoSubtitle","videoTags","videoTitle"]
                            },
        "videoJsonPlayer":{
                            "lastModified":"20/08/2015 07:48:43 +0200",
                            "videoDurationSeconds":5108,
                            "videoRemontageContenu":"A",
                            "videoIsoLang":"fr_FR",
                            "videoSwitchLang":{"de_DE":"055178-000_PLUS7-D"},
                            "programImage":"http://www.arte.tv/papi/tvguide/images/1450479/W940H530/055178-000-A_frauenoligarchen_02-1438051683414.jpg",
                            "videoRank":2,
                            "isLive":false,
                            "tracking":{
                                        "tablet":{
                                                    "ANDROID":"https://www.arte.tv/api/tracking/v1/055178-000/A/fr/TVGUIDE/TABLET/ANDROID/pixel.gif",
                                                    "IOS":"https://www.arte.tv/api/tracking/v1/055178-000/A/fr/TVGUIDE/TABLET/IOS/pixel.gif",
                                                    "WINDOWS_8":"https://www.arte.tv/api/tracking/v1/055178-000/A/fr/TVGUIDE/TABLET/WINDOWS_8/pixel.gif",
                                                    "WEB":"https://www.arte.tv/api/tracking/v1/055178-000/A/fr/TVGUIDE/TABLET/WEB/pixel.gif"
                                                },
                                        "tv":{
                                                    "ANDROID_TV_BOUYGUES":"https://www.arte.tv/api/tracking/v1/055178-000/A/fr/TVGUIDE/TV/ANDROID_TV_BOUYGUES/pixel.gif",
                                                    "PANASONIC":"https://www.arte.tv/api/tracking/v1/055178-000/A/fr/TVGUIDE/TV/PANASONIC/pixel.gif",
                                                    "PHILIPS":"https://www.arte.tv/api/tracking/v1/055178-000/A/fr/TVGUIDE/TV/PHILIPS/pixel.gif",
                                                    "SAMSUNG":"https://www.arte.tv/api/tracking/v1/055178-000/A/fr/TVGUIDE/TV/SAMSUNG/pixel.gif",
                                                    "XBOX":"https://www.arte.tv/api/tracking/v1/055178-000/A/fr/TVGUIDE/TV/XBOX/pixel.gif",
                                                    "FIRE_TV":"https://www.arte.tv/api/tracking/v1/055178-000/A/fr/TVGUIDE/TV/FIRE_TV/pixel.gif",
                                                    "VODAFONE":"https://www.arte.tv/api/tracking/v1/055178-000/A/fr/TVGUIDE/TV/VODAFONE/pixel.gif",
                                                    "HBBTV":"https://www.arte.tv/api/tracking/v1/055178-000/A/fr/TVGUIDE/TV/HBBTV/pixel.gif",
                                                    "ROKU":"https://www.arte.tv/api/tracking/v1/055178-000/A/fr/TVGUIDE/TV/ROKU/pixel.gif",
                                                    "HTML5":"https://www.arte.tv/api/tracking/v1/055178-000/A/fr/TVGUIDE/TV/HTML5/pixel.gif",
                                                    "TOSHIBA":"https://www.arte.tv/api/tracking/v1/055178-000/A/fr/TVGUIDE/TV/TOSHIBA/pixel.gif",
                                                    "LG":"https://www.arte.tv/api/tracking/v1/055178-000/A/fr/TVGUIDE/TV/LG/pixel.gif",
                                                    "ANDROID_TV":"https://www.arte.tv/api/tracking/v1/055178-000/A/fr/TVGUIDE/TV/ANDROID_TV/pixel.gif"
                                                    },
                                        "desktop":{
                                                    "WEB":"https://www.arte.tv/api/tracking/v1/055178-000/A/fr/TVGUIDE/DESKTOP/WEB/pixel.gif"
                                                    },
                                                    "mobile":{
                                                                "ANDROID":"https://www.arte.tv/api/tracking/v1/055178-000/A/fr/TVGUIDE/MOBILE/ANDROID/pixel.gif",
                                                                "APP":"https://www.arte.tv/api/tracking/v1/055178-000/A/fr/TVGUIDE/MOBILE/APP/pixel.gif",
                                                                "IOS":"https://www.arte.tv/api/tracking/v1/055178-000/A/fr/TVGUIDE/MOBILE/IOS/pixel.gif",
                                                                "WINDOWS_PHONE_8":"https://www.arte.tv/api/tracking/v1/055178-000/A/fr/TVGUIDE/MOBILE/WINDOWS_PHONE_8/pixel.gif",
                                                                "WEB":"https://www.arte.tv/api/tracking/v1/055178-000/A/fr/TVGUIDE/MOBILE/WEB/pixel.gif"
                                                            }
                                        },
                            "mobileAvailable":true,
                            "tvAvailable":true,
                            "pcAvailable":true,
                            "remontage":"A",
                            "videoPlayerUrl":"http://www.arte.tv/papi/tvguide/videos/stream/player/F/055178-000_PLUS7-F/ALL/ALL.json",
                            "videoWarning":false,
                            "caseProgram":"602_thema-mardi",
                            "genreProgram":"documentaire",
                            "postroll":"https://api.arte.tv/api/player/v1/recommendedPostroll/fr/055178-000-A?platform=ARTEPLUS7",
                            "genre":"Documentaire",
                            "videoBroadcastTimestamp":1439924043043,
                            "prereleased":false,
                            "infoProg":"(Allemagne/Israël, 2015, 86mn) ZDF",
                            "director":"Alexander Gentelev",
                            "productionYear":2015,
                            "conductor":true,
                            "VID":"055178-000_PLUS7-F",
                            "VTY":"ARTE_PLUS_SEVEN",
                            "VTI":"Poupées russes, diamants et grosses cylindrées",
                            "VDU":86,
                            "VTU":{
                                    "original":"http://www.arte.tv/papi/tvguide/images/1450479/ORIGINAL/055178-000-A_frauenoligarchen_02-1438051683414.jpg",
                                    "IID":"1450479",
                                    "IUR":"http://www.arte.tv/papi/tvguide/images/1450479/W940H530/055178-000-A_frauenoligarchen_02-1438051683414.jpg"
                                    },
                            "VCH":[{"channelID":"DOC","label":"Documentaire"}],
                            "VCM":[{"channelID":"DOU","label":"Documentaires / Magazines"}],
                            "VPO":1,
                            "VDA":"18/08/2015 20:50:00 +0200",
                            "VGB":"EUR_DE_FR",
                            "VRA":"18/08/2015 20:54:03 +0200",
                            "VRU":"17/09/2015 20:54:03 +0200",
                            "VAD":false,
                            "VVI":30522,
                            "VRT":0.0,
                            "VRC":true,
                            "VTR":"http://www.arte.tv/guide/fr/055178-000/poupees-russes-diamants-et-grosses-cylindrees",
                            "VDE":"Une fascinante étude du milieu fermé des oligarques russes, à travers le prisme de leurs relations conjugales : un monde où l'argent et le pouvoir modèlent les rapports entre les sexes. Dans un pays où les femmes restent encore largement écartées du pouvoir, ce documentaire dévoile les choix et les stratagèmes qu'elles doivent déployer pour arracher leur part du gâteau.",
                            "VED":false,
                            "VPR":false,
                            "VTA":["femme","Russie","richesse","divorce","oligarques"],
                            "VST":{
                                    "VNA":"poupees_russes_diamants_et_grosses_cylindrees",
                                    "VS1":"fr",
                                    "VS2":"602thema_mardi",
                                    "VS3":"ARTE7",
                                    "VS4":"055178-000",
                                    "VS5":"18082015",
                                    "VGE":"documentaire"
                                    },
                            "V7T":"Une fascinante étude du milieu fermé des oligarques russes, à travers le prisme de leurs relations conjugales.",
                            "VPI":"055178-000",
                            "VTX":"ARTE+7",
                            "VUP":"http://www.arte.tv/guide/fr/055178-000/poupees-russes-diamants-et-grosses-cylindrees",
                            "VTT":"https://www.arte.tv/api/tracking/v1/055178-000/A/fr/TVGUIDE/TV/HBBTV/pixel.gif",
                            "VMV":true,
                            "VCG":"Documentaire",
                            "VTH":["Stéréo","VF","16 / 9","HD natif"],
                            "VSR":{
                                    "HTTP_MP4_EQ_2":{
                                                    "quality":"MD - 400p",
                                                    "width":720,
                                                    "height":406,
                                                    "mediaType":"mp4",
                                                    "mimeType":"mp4",
                                                    "bitrate":1500,
                                                    "url":"http://arte.gl-systemhaus.de/am/tvguide/EUR_DE_FR/055178-000-A_EQ_2_VA_01932814_MP4-1500_AMM-Tvguide.mp4",
                                                    "videoFormat":"HBBTV",
                                                    "versionProg":"2",
                                                    "versionCode":"VA",
                                                    "versionLibelle":"Version allemande",
                                                    "versionShortLibelle":"VA",
                                                    "VQU":"EQ"
                                                    },
                                    "HTTP_MP4_EQ_1":{
                                                    "quality":"MD - 400p",
                                                    "width":720,
                                                    "height":406,
                                                    "mediaType":"mp4",
                                                    "mimeType":"mp4",
                                                    "bitrate":1500,
                                                    "url":"http://arte.gl-systemhaus.de/am/tvguide/EUR_DE_FR/055178-000-A_EQ_2_VF-STF_01932802_MP4-1500_AMM-Tvguide.mp4",
                                                    "videoFormat":"HBBTV",
                                                    "versionProg":"1",
                                                    "versionCode":"VF-STF",
                                                    "versionLibelle":"VF",
                                                    "versionShortLibelle":"VF",
                                                    "VQU":"EQ"
                                                    },
                                    "RTMP_LQ_2":{
                                                "quality":"LD - 220p",
                                                "width":384,
                                                "height":216,
                                                "mediaType":"rtmp",
                                                "mimeType":"mp4",
                                                "bitrate":300,
                                                "streamer":"rtmp://cp363648.edgefcs.net/ondemand/",
                                                "url":"am/tvguide/EUR_DE_FR/055178-000-A_MQ_2_VA_01932812_MP4-300_AMM-Tvguide.mp4",
                                                "videoFormat":"RMP4",
                                                "versionProg":"2",
                                                "versionCode":"VA",
                                                "versionLibelle":"Version allemande",
                                                "versionShortLibelle":"VA",
                                                "VQU":"MQ"
                                                },
                                    "HLS_EQ_1":{"mediaType":"hls",
                                                "mimeType":"mp4",
                                                "bitrate":1500,
                                                "url":"http://artehls-vh.akamaihd.net/i/am/tvguide/EUR_DE_FR/055178-000-A_2_VF-STF_AMM-Tvguide_XQ.6518727.smil/master.m3u8",
                                                "videoFormat":"M3U8",
                                                "versionProg":"1",
                                                "versionCode":"VF-STF",
                                                "versionLibelle":"VF",
                                                "versionShortLibelle":"VF","VQU":"SQ"
                                                },
                                    "RTMP_LQ_1":{
                                                "quality":"LD - 220p",
                                                "width":384,
                                                "height":216,
                                                "mediaType":"rtmp",
                                                "mimeType":"mp4",
                                                "bitrate":300,
                                                "streamer":"rtmp://cp363648.edgefcs.net/ondemand/",
                                                "url":"am/tvguide/EUR_DE_FR/055178-000-A_MQ_2_VF-STF_01932800_MP4-300_AMM-Tvguide.mp4",
                                                "videoFormat":"RMP4",
                                                "versionProg":"1",
                                                "versionCode":"VF-STF",
                                                "versionLibelle":"VF",
                                                "versionShortLibelle":"VF",
                                                "VQU":"MQ"
                                                },
                                    "HLS_SQ_2":{
                                                "quality":"MD - 400p",
                                                "width":640,
                                                "height":360,
                                                "mediaType":"hls",
                                                "mimeType":"mp4",
                                                "bitrate":2200,
                                                "url":"http://artehls-vh.akamaihd.net/i/am/tvguide/EUR_DE_FR/055178-000-A_2_VA_AMM-Tvguide_XQ.6518832.smil/master.m3u8",
                                                "videoFormat":"M3U8",
                                                "versionProg":"2",
                                                "versionCode":"VA",
                                                "versionLibelle":"Version allemande",
                                                "versionShortLibelle":"VA",
                                                "VQU":"SQ"
                                                },
                                    "RTMP_SQ_1":{
                                                "quality":"HD - 720p",
                                                "width":1280,
                                                "height":720,
                                                "mediaType":"rtmp",
                                                "mimeType":"mp4",
                                                "bitrate":2200,
                                                "streamer":"rtmp://cp363648.edgefcs.net/ondemand/",
                                                "url":"am/tvguide/EUR_DE_FR/055178-000-A_SQ_2_VF-STF_01932808_MP4-2200_AMM-Tvguide.mp4",
                                                "videoFormat":"RMP4",
                                                "versionProg":"1",
                                                "versionCode":"VF-STF",
                                                "versionLibelle":"VF",
                                                "versionShortLibelle":"VF",
                                                "VQU":"SQ"
                                                },
                                    "RTMP_SQ_2":{
                                                "quality":"HD - 720p",
                                                "width":1280,
                                                "height":720,
                                                "mediaType":"rtmp",
                                                "mimeType":"mp4",
                                                "bitrate":2200,
                                                "streamer":"rtmp://cp363648.edgefcs.net/ondemand/",
                                                "url":"am/tvguide/EUR_DE_FR/055178-000-A_SQ_2_VA_01932816_MP4-2200_AMM-Tvguide.mp4",
                                                "videoFormat":"RMP4",
                                                "versionProg":"2",
                                                "versionCode":"VA",
                                                "versionLibelle":"Version allemande",
                                                "versionShortLibelle":"VA",
                                                "VQU":"SQ"
                                                },
                                    "HTTP_MP4_LQ_2":{
                                                    "quality":"LD - 220p",
                                                    "mediaType":"mp4",
                                                    "mimeType":"mp4",
                                                    "bitrate":300,
                                                    "url":"http://arte.gl-systemhaus.de/am/tvguide/EUR_DE_FR/055178-000-A_MQ_2_VA_01932812_MP4-300_AMM-Tvguide.mp4",
                                                    "videoFormat":"HBBTV",
                                                    "versionProg":"2",
                                                    "versionCode":"VA",
                                                    "versionLibelle":"Version allemande",
                                                    "versionShortLibelle":"VA",
                                                    "VQU":"MQ"
                                                    },
                                    "HTTP_MP4_LQ_1":{
                                                    "quality":"LD - 220p",
                                                    "mediaType":"mp4",
                                                    "mimeType":"mp4",
                                                    "bitrate":300,
                                                    "url":"http://arte.gl-systemhaus.de/am/tvguide/EUR_DE_FR/055178-000-A_MQ_2_VF-STF_01932800_MP4-300_AMM-Tvguide.mp4",
                                                    "videoFormat":"HBBTV",
                                                    "versionProg":"1",
                                                    "versionCode":"VF-STF",
                                                    "versionLibelle":"VF",
                                                    "versionShortLibelle":"VF",
                                                    "VQU":"MQ"
                                                    },
                                    "HTTP_MP4_SQ_2":{
                                                    "quality":"HD - 720p",
                                                    "width":1280,
                                                    "height":720,
                                                    "mediaType":"mp4",
                                                    "mimeType":"mp4",
                                                    "bitrate":2200,
                                                    "url":"http://arte.gl-systemhaus.de/am/tvguide/EUR_DE_FR/055178-000-A_SQ_2_VA_01932816_MP4-2200_AMM-Tvguide.mp4",
                                                    "videoFormat":"HBBTV",
                                                    "versionProg":"2",
                                                    "versionCode":"VA",
                                                    "versionLibelle":"Version allemande",
                                                    "versionShortLibelle":"VA",
                                                    "VQU":"SQ"
                                                                },
                                    "RTMP_EQ_1":{
                                                        "quality":"MD - 400p",
                                                        "width":720,
                                                        "height":406,
                                                        "mediaType":"rtmp","mimeType":"mp4",
                                                        "bitrate":1500,
                                                        "streamer":"rtmp://cp363648.edgefcs.net/ondemand/",
                                                        "url":"am/tvguide/EUR_DE_FR/055178-000-A_EQ_2_VF-STF_01932802_MP4-1500_AMM-Tvguide.mp4",
                                                        "videoFormat":"RMP4",
                                                        "versionProg":"1",
                                                        "versionCode":"VF-STF",
                                                        "versionLibelle":"VF",
                                                        "versionShortLibelle":"VF",
                                                        "VQU":"EQ"
                                                        },
                                    "RTMP_MQ_1":{
                                                        "quality":"SD - 400p",
                                                        "width":720,
                                                        "height":406,
                                                        "mediaType":"rtmp",
                                                        "mimeType":"mp4",
                                                        "bitrate":800,
                                                        "streamer":"rtmp://cp363648.edgefcs.net/ondemand/",
                                                        "url":"am/tvguide/EUR_DE_FR/055178-000-A_HQ_2_VF-STF_01932801_MP4-800_AMM-Tvguide.mp4",
                                                        "videoFormat":"RMP4",
                                                        "versionProg":"1",
                                                        "versionCode":"VF-STF",
                                                        "versionLibelle":"VF",
                                                        "versionShortLibelle":"VF",
                                                        "VQU":"HQ"
                                                        },
                                    "RTMP_MQ_2":{
                                                        "quality":"SD - 400p",
                                                        "width":720,
                                                        "height":406,
                                                        "mediaType":"rtmp",
                                                        "mimeType":"mp4",
                                                        "bitrate":800,
                                                        "streamer":"rtmp://cp363648.edgefcs.net/ondemand/",
                                                        "url":"am/tvguide/EUR_DE_FR/055178-000-A_HQ_2_VA_01932813_MP4-800_AMM-Tvguide.mp4",
                                                        "videoFormat":"RMP4",
                                                        "versionProg":"2",
                                                        "versionCode":"VA",
                                                        "versionLibelle":"Version allemande",
                                                        "versionShortLibelle":"VA",
                                                        "VQU":"HQ"
                                                        },
                                    "RTMP_EQ_2":{
                                                        "quality":"MD - 400p",
                                                        "width":720,"height":406,
                                                        "mediaType":"rtmp","mimeType":"mp4",
                                                        "bitrate":1500,
                                                        "streamer":"rtmp://cp363648.edgefcs.net/ondemand/",
                                                        "url":"am/tvguide/EUR_DE_FR/055178-000-A_EQ_2_VA_01932814_MP4-1500_AMM-Tvguide.mp4",
                                                        "videoFormat":"RMP4",
                                                        "versionProg":"2",
                                                        "versionCode":"VA",
                                                        "versionLibelle":"Version allemande",
                                                        "versionShortLibelle":"VA","VQU":"EQ"
                                                        },
                                    "HTTP_MP4_MQ_1":{
                                                                "quality":"SD - 400p",
                                                                "width":720,
                                                                "height":406,
                                                                "mediaType":"mp4",
                                                                "mimeType":"mp4",
                                                                "bitrate":800,
                                                                "url":"http://arte.gl-systemhaus.de/am/tvguide/EUR_DE_FR/055178-000-A_HQ_2_VF-STF_01932801_MP4-800_AMM-Tvguide.mp4",
                                                                "videoFormat":"HBBTV",
                                                                "versionProg":"1",
                                                                "versionCode":"VF-STF",
                                                                "versionLibelle":"VF",
                                                                "versionShortLibelle":"VF",
                                                                "VQU":"HQ"
                                                                },
                                    "HTTP_MP4_SQ_1":{
                                                                "quality":"HD - 720p",
                                                                "width":1280,
                                                                "height":720,
                                                                "mediaType":"mp4",
                                                                "mimeType":"mp4",
                                                                "bitrate":2200,
                                                                "url":"http://arte.gl-systemhaus.de/am/tvguide/EUR_DE_FR/055178-000-A_SQ_2_VF-STF_01932808_MP4-2200_AMM-Tvguide.mp4",
                                                                "videoFormat":"HBBTV",
                                                                "versionProg":"1",
                                                                "versionCode":"VF-STF",
                                                                "versionLibelle":"VF",
                                                                "versionShortLibelle":"VF",
                                                                "VQU":"SQ"
                                                                },
                                    "HTTP_MP4_MQ_2":{
                                                                "quality":"SD - 400p",
                                                                "width":720,"height":406,"mediaType":"mp4",
                                                                "mimeType":"mp4",
                                                                "bitrate":800,
                                                                "url":"http://arte.gl-systemhaus.de/am/tvguide/EUR_DE_FR/055178-000-A_HQ_2_VA_01932813_MP4-800_AMM-Tvguide.mp4"
                                                                ,"videoFormat":"HBBTV",
                                                                "versionProg":"2","versionCode":"VA",
                                                                "versionLibelle":"Version allemande",
                                                                "versionShortLibelle":"VA",
                                                                "VQU":"HQ"
                                                                }
                                    },
                                "VPG":"2",
                                "VPC":"602",
                                "VLA":"F"}
            }
            
## ------
print "---- TEST JSON MODULE ----"
obj_json=str(dico)
print obj_json
obj=json.loads(obj_json)
#print obj

#print dico
print type(dico)
print dico.keys()
# il y a deux clefs
for k in dico.keys():
    print k
print dico[dico.keys()[1]].keys()
print "---------\n"
print dico['videoJsonPlayer']['VSR']
for k in dico['videoJsonPlayer']['VSR'].keys():
    print k
#ce que l'on cherche se trouve sous dico 'videoJsonPlayer'
for val in dico['videoJsonPlayer']['VSR'].values():
    print "val is: %s" %val['url']
