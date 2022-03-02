from django.contrib import admin
from .models import Author, Book, BookInstance, Genre

# Register your models here.


class BookInline(admin.TabularInline):
    model = Book


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ("last_name", "first_name", "date_of_birth", "date_of_death")

    fields = ["first_name", "last_name", ("date_of_birth", "date_of_death")]

    inlines = [BookInline]


@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_display = ("status", "due_back", "id")
    list_filter = ("status", "due_back")

    fieldsets = (
        (None, {"fields": ("book", "inprint", "id")}),
        ("Availability", {"fields": ("status", "due_back")}),
    )


class BooksInstanceInline(admin.TabularInline):
    model = BookInstance


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "display_genre")

    inlines = [BooksInstanceInline]