
# mercury/views.py
@api_view(['POST'])
@is_authenticated_admin
def mass_email(request):
    logger.debug("Sending mass email")
    failures = []
    has_attachment = request.data["attachment"]

    if has_attachment == 1:
        uf = UploadedFile.objects.get(unique_id=request.data['attachment_uid'])
        mimetype = mimetypes.guess_type(request.data["attachment_name"])[
            0] or 'application/octet-stream'

        attachment_data = {
            "content": base64.b64encode(uf.file.read()).decode(),
            "type": mimetype,
            "filename": request.data['attachment_name'],
            "disposition": "attachment",
            "content_id": uf.unique_id,
        }

    try:
        max_recipients = int(GlobalSetting.objects.get(
            key="MassEmailMaximum", r_update_time__gt=datetime.utcnow() - timedelta(hours=12)).value)
    except:
        max_recipients = 5

    if len(request.data['recipient_emails']) > max_recipients:
        return Response({"status": 99, "message": "Please adjust MassEmailMaximum in admin"})

    if has_attachment == 1:
        failures = mass_email_async(request.data['recipient_emails'], request.data['invite_text'],
                                    request.data['subject_text'], request.data['cc_email'], request.data['reply_to'], attachment_data)
    else:
        failures = mass_email_async(request.data['recipient_emails'], request.data['invite_text'],
                                    request.data['subject_text'], request.data['cc_email'], request.data['reply_to'])

    if len(failures) > 0:
        return Response({"status": 99, "message": "Error sending invite to " + ", ".join(failures)})

    return Response({"status": 200, "message": "Success!"})

# mercury/views.py (same)
@job('jango')
def mass_email_async(emails, invite_text, subject_text, cc_email, reply_to, attachment_data=None):
    failures = []
    for email in emails:
        try:
            if attachment_data == None:
                mail_monkey(email, invite_text,
                            subject_text, cc_email, reply_to)
            else:
                mail_monkey(email, invite_text, subject_text,
                            cc_email, reply_to, attachment_data)

            logger.info("The e-mail succeeded")
            sleep(1)
        except:
            failures.append(email)
            logger.info("The e-mail failed")

    if len(failures) > 0:
        return Response({"status": 99, "message": "Error sending invite to " + ", ".join(failures)})
    return Response({"status": 200, "message": "Success!"})




# iv_emails/models.py
def mail_monkey(email_address, message_text, subject, cc_to, reply_to, attachment_data=None):

    paragraphs = message_text.replace("\n\n", "\n").split("\n")
    email_address = email_address
    subject = subject
    logger.info("Mail_monkey was called")

    try:
        logger.info("Email stylizer was attempted")
        if cc_to == "":
            cc_to = None
        if reply_to == "":
            reply_to = None

        email_stylizer(paragraphs, email_address, subject,
                       cc_to, reply_to, attachment_data)

        logger.info("email stylizer succeeded")

    except Exception as e:
        logger.exception(e)

# iv_emails/models.py (same)
def email_stylizer(paragraph, email_address, subject, cc_to, reply_to, attachment_data):

    subject = subject
    email_address = email_address
    logger.info("email stylizer was called")

    boldActive = False
    italicActive = False
    underlineActive = False
    urlActive = False
    bullet = False
    for y in range(len(paragraph)):
        paragin = paragraph[y]
        paragin = escape(paragin)
        paragout = ""
        bullet = False
        for x in range(len(paragin)):  # for each character in the paragraph
            # print(paragout) (for debugging)
            # print(urlActive)
            # print(paragin[x])
            if paragin[x] == "&" and paragin[x+1] == "g" and paragin[x+2] == "t" and paragin[x+3] == ";":
                urlActive = False
            if urlActive == False:
                if paragin[x] == "-" and x == 0:
                    paragout = "<ul><li>"
                    bullet = True
                elif paragin[x] == "&" and paragin[x+1] == "l" and paragin[x+2] == "t" and paragin[x+3] == ";":
                    urlActive = True
                elif paragin[x] == "*":
                    if boldActive == False:
                        paragout = paragout + "<b>"
                        boldActive = not boldActive
                    else:
                        paragout = paragout + "</b>"
                        boldActive = not boldActive
                elif paragin[x] == "_":
                    if italicActive == False:
                        paragout = paragout + "<i>"
                        italicActive = not italicActive
                    else:
                        paragout = paragout + "</i>"
                        italicActive = not italicActive
                elif paragin[x] == "~":
                    if underlineActive == False:
                        paragout = paragout + "<u>"
                        underlineActive = not underlineActive
                    else:
                        paragout = paragout + "</u>"
                        underlineActive = not underlineActive
                else:
                    paragout = paragout + paragin[x]
                    if bullet == True and x + 1 == len(paragin):
                        paragout = paragout + "</li></ul>"
            if urlActive == True:
                paragout = paragout + paragin[x]

        urlEndpoints = []
        for x in range(len(paragout)):
            if paragout[x] == "&" and paragout[x+2] == "t" and paragout[x+3] == ";":
                logger.info(f"Found url endpoint at {x}")
                urlEndpoints.append(x)
        urlEndpoints.sort(reverse=True)
        for endpt in urlEndpoints:
            logger.info(f"Working with endpoint at {endpt} and parag {paragout}")
            
            paragout = paragout[0:endpt] + paragout[endpt+4:]
            logger.info(f"Parag now {paragout}")

        paragraph[y] = paragout

    context = {
        "paragraphs": paragraph
    }

    content = render_to_string("mass_email.html", context)
    logger.info(content)

    try:
        logger.info("sending email was tried")
        send_mail_async.delay(subject, SENDER_ADDRESS, email_address, html_text=content,
                              reply_to=reply_to, cc_to=cc_to, attachment_data=attachment_data)
        logger.info("sending email succeeded")
    except Exception as e:
        logger.exception(e)
        logger.info("the email failed models.py exception line 478")
