from models import *
import db
import os


if __name__ == "__main__":
    # テーブル作成
    Base.metadata.create_all(db.ENGINE)

    # CRUD
    # INSERT
    print('--- INSERT ---')
    user = User(username='hoge', password='p@ssW0rd', mail='hoge@example.com')
    db.session.add(user)
    db.session.commit()
    print(user)

    task = Task(
        user_id=user.id,
        content='New Task 1',
        deadline=datetime(2021, 1, 1, 10, 30, 15),
    )
    db.session.add(task)
    db.session.commit()
    print(task)

    task = Task(
        user_id=user.id,
        content='New Task 2',
        deadline=datetime(2021, 2, 1, 10, 30, 15),
    )
    db.session.add(task)
    db.session.commit()
    print(task)

    # UPDATE
    print('--- UPDATE ---')
    task = db.session.query(Task).filter(Task.user_id == user.id).first()
    task.done = True
    db.session.commit()
    print(task)

    # DELETE
    print('--- DELETE ---')
    task = db.session.query(Task).filter(Task.content == 'New Task 2').first()
    print(task)
    db.session.delete(task)
    db.session.commit()

    # SELECT
    print('--- SELECT ---')
    admins = db.session.query(User).all()
    for admin in admins:
        print(admin)
    tasks = db.session.query(Task).all()
    for task in tasks:
        print(task)
