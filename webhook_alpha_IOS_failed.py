from json import dumps
from datetime import datetime, timezone
from httplib2 import Http




def main():
    message_headers = {'Content-Type': 'application/json; charset=UTF-8'}
    test_url =  'https://chat.googleapis.com/v1/spaces/AAAACmWw6q8/messages?key=AIzaSyDdI0hCZtE6vySjMm-WEfRq3CPzqKqqsHI&token=ly36Lxs0rOMA2c6nJzeIwE1lfU3gQjCQ3A6sCgRSRB4%3D'
    prod_url = 'https://chat.googleapis.com/v1/spaces/AAAA6ed3_G8/messages?key=AIzaSyDdI0hCZtE6vySjMm-WEfRq3CPzqKqqsHI&token=Gx4ifThVUky0TxiYlaFouyBsL5GoPNrt9SpKZ4JIRnE%3D'
    bot_message = { 'text': f"""------------NEWS---------------
*Your Bitrise Deploy Failed* 
*Date and Time*: {datetime.now().strftime("%d/%m/%Y - %H:%M:%S")}   
*Platform*: *IOS*
*Workflow*: *Alpha*
*Full dashboard Link*: https://app.bitrise.io/dashboard
"""}



     
    message_headers = {'Content-Type': 'application/json; charset=UTF-8'}
    http_obj = Http()
    response = http_obj.request(
        uri=test_url,
        method='POST',
        headers=message_headers,
        body=dumps(bot_message),
    )
    print(response)


if __name__ == '__main__':
    main()

    #   - run:
    #       name: Google Chat Fail Notification
    #       when: on_fail
    #       command: |
    #         curl --header "Content-Type: application/json" \
    #         --request POST \
    #         --data "{\"cards\":[{\"header\":{\"title\":\"Ops! ${CIRCLE_JOB} failed.\",\"subtitle\":\"${CIRCLE_PROJECT_REPONAME}-${CIRCLE_BRANCH}\",\"imageUrl\":\"https://png.pngtree.com/svg/20170406/icon_failed__1325447.png\",\"imageStyle\":\"IMAGE\"},\"sections\":[{\"widgets\":[{\"keyValue\":{\"topLabel\":\"${CIRCLE_TAG}\",\"content\":\"Credits - ${CIRCLE_USERNAME}\"}}]},{\"widgets\":[{\"buttons\":[{\"textButton\":{\"text\":\"DETAILS\",\"onClick\":{\"openLink\":{\"url\":\"${CIRCLE_BUILD_URL}\"}}}}]}]}]}]}" \
    #         "$CHAT_INFRA"
    #   - run:
    #       name: Google Chat Successful Notification
    #       when: on_success
    #       command: |
    #         curl --header "Content-Type: application/json" \
    #         --request POST \
    #         --data "{\"cards\":[{\"header\":{\"title\":\"${CIRCLE_JOB} successful.\",\"subtitle\":\"${CIRCLE_PROJECT_REPONAME}-${CIRCLE_BRANCH}\",\"imageUrl\":\"https://cdn.dribbble.com/users/314596/screenshots/3241132/media/8e2907a9f80400ee3f40865a3803e6c3.gif\",\"imageStyle\":\"IMAGE\"},\"sections\":[{\"widgets\":[{\"keyValue\":{\"topLabel\":\"${CIRCLE_TAG}\",\"content\":\"Credits - ${CIRCLE_USERNAME}\"}}]},{\"widgets\":[{\"buttons\":[{\"textButton\":{\"text\":\"DETAILS\",\"onClick\":{\"openLink\":{\"url\":\"${CIRCLE_BUILD_URL}\"}}}}]}]}]}]}" \
    #         "$CHAT_INFRA"
