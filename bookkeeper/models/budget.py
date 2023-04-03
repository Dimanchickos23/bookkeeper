from dataclasses import dataclass, field
from datetime import datetime


@dataclass(slots=True)
class Budget:
    """
        Выделяемый бюджет.
        amount - сумма
        category - id бюджета на категорию
        added_date - дата добавления в бд
        comment - комментарий
        pk - id записи в базе данных
        """
    amount: int
    category: int
    added_date: datetime = field(default_factory=datetime.now)
    comment: str = ''
    pk: int = 0