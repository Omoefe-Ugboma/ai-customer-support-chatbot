from app.models.chat_thread import ChatThread
from app.models.chat_message import ChatMessage


# =========================
# CREATE THREAD
# =========================
def create_thread(
    db,
    user_id,
):

    thread = ChatThread(
        user_id=user_id,
    )

    db.add(thread)

    db.commit()

    db.refresh(thread)

    return thread


# =========================
# GET THREADS
# =========================
def get_threads(
    db,
    user_id,
):

    return (
        db.query(ChatThread)
        .filter(
            ChatThread.user_id == user_id
        )
        .order_by(
            ChatThread.created_at.desc()
        )
        .all()
    )


# =========================
# GET THREAD
# =========================
def get_thread(
    db,
    thread_id,
    user_id,
):

    return (
        db.query(ChatThread)
        .filter(
            ChatThread.id == thread_id,
            ChatThread.user_id == user_id,
        )
        .first()
    )


# =========================
# SAVE MESSAGE
# =========================
def save_thread_message(
    db,
    thread_id,
    role,
    content,
):

    message = ChatMessage(
        role=role,
        content=content,
        thread_id=thread_id,
    )

    db.add(message)

    db.commit()

    return message


# =========================
# DELETE THREAD
# =========================
def delete_thread(
    db,
    thread_id,
    user_id,
):

    thread = get_thread(
        db,
        thread_id,
        user_id,
    )

    if not thread:
        return False

    db.delete(thread)

    db.commit()

    return True


# =========================
# RENAME THREAD
# =========================
def rename_thread(
    db,
    thread_id,
    user_id,
    title,
):

    thread = get_thread(
        db,
        thread_id,
        user_id,
    )

    if not thread:
        return None

    thread.title = title

    db.commit()

    db.refresh(thread)

    return thread