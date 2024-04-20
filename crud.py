from sqlalchemy.orm import Session
from models import Book, Author
from schemas import BookCreate, AuthorCreate


def get_all_authors(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Author).offset(skip).limit(limit).all()


def get_author_by_name(db: Session, name: str):
    return (
        db.query(Author)
        .filter(Author.name == name)
        .first()
    )


def get_author(db: Session, author_id: int):
    return (
        db.query(Author)
        .filter(Author.id == author_id)
        .first()
    )


def create_author(db: Session, author: AuthorCreate):
    db_author = Author(
        name=author.name,
        bio=author.bio,
    )
    db.add(db_author)
    db.commit()
    db.refresh(db_author)

    return db_author


def get_all_books(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Book).offset(skip).limit(limit).all()


def get_book(db: Session, book_id: int):
    return (
        (db.query(Book))
        .filter(Book.id == book_id)
        .first()
    )


def create_book(db: Session, book: BookCreate):
    db_book = Book(
        title=book.title,
        summary=book.summary,
        publication_date=book.publication_date,
        author_id=book.author_id,
    )
    db.add(db_book)
    db.commit()
    db.refresh(db_book)

    return db_book
