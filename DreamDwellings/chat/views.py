from django.shortcuts import render, redirect, get_object_or_404
from .models import Chat, ChatRoom

def chat_rooms(request):
    chat_rooms = ChatRoom.objects.all()
    return render(request, 'chat/chat_rooms.html', {'chat_rooms': chat_rooms})

def chat_messages(request, room_id):
    room = get_object_or_404(ChatRoom, id=room_id)
    messages = Chat.objects.filter(room=room)
    return render(request, 'chat/chat_messages.html', {'room': room, 'messages': messages})

def create_message(request, room_id):
    if request.method == 'POST':
        content = request.POST.get('content')
        room = ChatRoom.objects.get(id=room_id)
        user = request.user
        Chat.objects.create(content=content, user=user, room=room)
        return redirect('chat:chat_messages', room_id=room_id)
    else:
        # Handle GET requests (if necessary)
        pass