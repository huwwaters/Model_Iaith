for i in {0..7000}
do
    wget "https://cofnod.cynulliad.cymru/XMLExport/Download?meetingID=$i&xmlDownloadType=BilingualTranscript" -P "/Users/huwwaters/Documents/Y Cofnod/Dwyieithog"
done