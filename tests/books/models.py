from django.db.models import Model, CharField, IntegerField, Func, F

from django_plpy.installer import plfunction, pltrigger


@plfunction
def pl_max(a: int, b: int) -> int:
    if a > b:
        return a
    return b


class Book(Model):
    name = CharField(max_length=100)
    amount_stock = IntegerField(default=20)
    amount_sold = IntegerField(default=10)
    stock_days_left = IntegerField(null=True, blank=True)

    def get_max(self):
        return (
            Book.objects.annotate(
                max_value=Func(F("amount_sold"), F("amount_stock"), function="pl_max")
            )
            .get(pk=self.pk)
            .max_value
        )


@pltrigger(event="UPDATE", when="BEFORE", model=Book)
def pl_update_amount(new: Book, old: Book, td, plpy):
    # don't use save method here, it will kill the database because of recursion
    new.amount_stock += 10


@pltrigger(event="UPDATE", when="BEFORE", model=Book)
def stock_days_left(new: Book, old: Book, td, plpy):
    # don't use save method here, it will kill the database because of recursion
    new.stock_days_left = int(new.amount_stock / new.amount_sold)
