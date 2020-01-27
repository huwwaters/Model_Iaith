for f in Download?meetingID=*; do mv $f ${f/Download?meetingID=/Saesneg_Cyfarfod_}; done

for f in *"&xmlDownloadType=WelshTranscript"; do mv $f ${f/"&xmlDownloadType=WelshTranscript"/.xml}; done
for f in *"&xmlDownloadType=EnglishTranscript"; do mv $f ${f/"&xmlDownloadType=EnglishTranscript"/.xml}; done


for f in *"&xmlDownloadType=WelshTranscript"; do mv $f ${f/"&xmlDownloadType=WelshTranscript"/.xml}; done

#Dwyieithog_Cyfarfod_3608&xmlDownloadType=BilingualTranscript

for f in Download?meetingID=*; do mv $f ${f/Download?meetingID=/Saesneg_Cyfarfod_}; done
for f in *"&xmlDownloadType=EnglishTranscript"; do mv $f ${f/"&xmlDownloadType=EnglishTranscript"/.xml}; done