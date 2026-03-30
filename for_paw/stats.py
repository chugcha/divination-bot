import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
from io import BytesIO
from typing import Tuple, Optional

def all_stats(user_id: int) -> Tuple[str, Optional[BytesIO]]:
    con = sqlite3.connect('divinations.db')
    query_user = '''
        SELECT b.title, COUNT(*) as cnt
        FROM Predictions p
        JOIN Books b ON p.book_id = b.book_id
        WHERE p.user_id = ?
        GROUP BY b.book_id
        ORDER BY cnt DESC
        LIMIT 5
    '''
    df_user = pd.read_sql_query(query_user, con, params=(user_id,))
    query_all = '''
        SELECT b.title, COUNT(*) as cnt
        FROM Predictions p
        JOIN Books b ON p.book_id = b.book_id
        GROUP BY b.book_id
        ORDER BY cnt DESC
        LIMIT 5
    '''
    df_all = pd.read_sql_query(query_all, con)
    con.close()
    messages = []
    if not df_user.empty:
        messages.append(
            f"Вы чаще всего выбирали '{df_user.iloc[0]['title']}' "
            f"({df_user.iloc[0]['cnt']} раз)"
        )
    if not df_all.empty:
        messages.append(
            f"Самая популярная книга среди пользователей: '{df_all.iloc[0]['title']}' "
            f"({df_all.iloc[0]['cnt']} раз)"
        )
    text_result = '\n'.join(messages) if messages else 'Пока нет данных:('
    if df_user.empty and df_all.empty:
        return text_result, None
    fig, axes = plt.subplots(1, 2, figsize=(14, 6))
    if not df_user.empty:
        axes[0].barh(df_user['title'], df_user['cnt'])
        axes[0].set_title('Ваши книги')
    if not df_all.empty:
        axes[1].barh(df_all['title'], df_all['cnt'])
        axes[1].set_title('Популярные книги')
    plt.tight_layout()
    buf = BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    plt.close()
    return text_result, buf
