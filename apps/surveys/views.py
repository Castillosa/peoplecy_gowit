# import uuid
#
# from django.http import JsonResponse
# from django.shortcuts import render
# from django.views.decorators.csrf import csrf_exempt
#
# from apps.surveys.exceptions import WrongQuestionTypeException, NotRelatedAnswerException, \
#     WrongAnswerTypeException, NotRelatedQuestionException
# from apps.surveys.models import SurveyAnswer
#
#
# def get_enps_profile_question(questions, step, batch, sender_uid):
#     related_answer = questions[0].get_related_answer(batch, sender_uid)
#     if not related_answer:
#         raise NotRelatedAnswerException()
#
#     # related_answer needs to be enps type
#     if related_answer.question.type != 'enps':
#         raise WrongQuestionTypeException()
#
#     try:
#         value = int(related_answer.value)
#     except ValueError:
#         raise WrongAnswerTypeException()
#     question = None
#     if value > 8:
#         question = questions.get(order=step, enps_filter='promoters')
#     elif 6 < value < 9:
#         question = questions.get(order=step, enps_filter='neutrals')
#     elif value < 6:
#         question = questions.get(order=step, enps_filter='detractors')
#
#     if question is None:
#         raise NotRelatedQuestionException()
#     return question
#
#
# #TODO: en el envio de emails / sms se enviara el senderType y senderUID
# @csrf_exempt
# def get_survey(request, batch_hash_id, sender_type_uid=None, sender_uid=None, step=0):
#     # batch = SurveyBatch.objects.get(hash_id=batch_hash_id)
#     survey = None
#     answer = None
#     #TODO: check if batch-sender_UID is already answered
#     try:
#         answer = SurveyAnswer.objects.get(sender_uid=sender_uid, answer_order=step)
#     except SurveyAnswer.DoesNotExist:
#         pass
#     next_step = step + 1
#     max_step = survey.steps()
#     if step == 0:
#         # if batch.is_anonymous:
#         #     sender_type_uid = SENDER_TYPE_CHOICES_UUID['anonymous']
#         #     sender_uid = uuid.uuid4()
#         return render(request, 'surveys/index.html',
#                       {'survey': survey,
#                        "company": survey.company,
#                        "text": survey.texto1,
#                        "subtext": survey.texto2,
#                        'step': step,
#                        'next_step': next_step,
#                        # 'batch_hash_id': batch.hash_id,
#                        'sender_type_uid': sender_type_uid,
#                        'sender_uid': sender_uid})
#
#     if step <= max_step:
#
#         questions = survey.surveyquestion_set.filter(order=step)
#         question_order_len = len(questions)
#         question = questions[0]
#         if question_order_len > 1:
#             # question = get_enps_profile_question(questions, step, batch, sender_uid)
#
#         widget_template = 'surveys/widgets/%s.html' % question.type
#
#         return render(request, widget_template,
#                       {
#                        'survey': survey,
#                        'step': step,
#                        'back_step': step - 1,
#                        "edit_mode": True if answer else False,
#                        'answer': answer,
#                        'next_step': next_step,
#                        'components': question.get_components() if question.type == 'components' else None,
#                        'attributes': question.get_attributes() if question.type == 'attributes' else None,
#                        'questions_set': questions,
#                        # 'batch': batch,
#                        'question': question,
#                        'sender_type_uid': sender_type_uid,
#                        'sender_uid': sender_uid,
#                        })
#
#     return render(request, "surveys/thanks.html",
#                   {'company': survey.company,
#                    'step': step,
#                    'back_step': step - 1,
#                    # 'batch': batch,
#                    'sender_type_uid': sender_type_uid,
#                    'sender_uid': sender_uid,
#                    })
#
#
# def edit_answer(request):
#     answer = SurveyAnswer.objects.get(id=request.POST.get('answer_id'))
#     answer.value = request.POST.get('answer_value')
#     answer.extra_data = request.POST.get('extra_data') if request.POST.get('extra_data') else None
#     try:
#         answer.save()
#         return JsonResponse({'status': 'ok'})
#     except Exception as e:
#         return JsonResponse({'status': 'fail', 'error': str(e)})
#
# @csrf_exempt
# def post_answer(request):
#     if request.method == 'POST':
#         edit_mode = request.POST.get('edit_mode')
#         if edit_mode == 'True':
#             return edit_answer(request)
#         print(edit_mode)
#         answer = SurveyAnswer()
#         answer.question_id = request.POST.get('question_id')
#         answer.value = request.POST.get('answer_value')
#         answer.question_type = request.POST.get('question_type')
#         answer.answer_order = request.POST.get('question_order')
#
#         answer.batch_id = request.POST.get('batch_id')
#         answer.enps_profile = request.POST.get('enps_profile') if request.POST.get('enps_profile') else None
#         answer.extra_data = request.POST.get('extra_data') if request.POST.get('extra_data') else None
#         try:
#             answer.save()
#             return JsonResponse({'status': 'ok'})
#         except Exception as e:
#             return JsonResponse({'status': 'fail', 'error': str(e)})
