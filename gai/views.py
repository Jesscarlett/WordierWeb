from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
import google.generativeai as ggai
import markdown
from django.utils.safestring import mark_safe
from dictionary.config import KEY
from .serializers import ChatRequestSerializer, ChatResponseSerializer


class GenerateResponseView(APIView):

    def post(self, request):
        ggai.configure(api_key=KEY)
        generation_config = {
            "temperature": 2,
            "top_p": 0.95,
            "top_k": 64,
            "max_output_tokens": 8192,
            "response_mime_type": "text/plain",
        }
        serializer = ChatRequestSerializer(data=request.data)
        if serializer.is_valid():
            message = serializer.validated_data['message']

            # Replace with your Google Generative AI API key and model
            model_name = "gemini-1.5-flash"  # Replace with your desired model name

            model = ggai.GenerativeModel(model_name=model_name, generation_config=generation_config)
            generated_text = model.generate_content(message).text
            generated_text = generated_text.replace('## ', '**').replace('# ', '*')
            response_message = mark_safe(markdown.markdown(generated_text))
            return Response({'response': response_message}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)