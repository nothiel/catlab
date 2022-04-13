from pydantic import BaseModel
from datetime import datetime


class CatSchema(BaseModel):
    cat_name: str
    cat_birth_date: datetime
    cat_vaccined: bool
    cat_castrated: bool
    cat_photos: list

class CatsSchema(BaseModel):
    cats: list[CatSchema]

class CatModifySchema(BaseModel):
    cat_vaccined: bool | None = None
    cat_castrated: bool | None = None 
    cat_photos: list | None = None


# [
#   {
#     _id: ObjectId("6250f00a8336b572ed3b5b11"),
#     full_name: 'Rafael Luis Barbosa',
#     birth_date: ISODate("1998-11-16T00:00:00.000Z"),
#     email: 'rafaellb2555@gmail.com',
#     username: 'nothielf',
#     hashed_password: '$2b$12$eIbutc7PxdO6VubXSyj5gua/Jlm4tpnjZB4jUveLRLXklF6YUTZeO',
#     cats: [
#       {
#         cat_name: 'Loki',
#         cat_birth_date: ISODate("2021-11-02T00:00:00.000Z"),
#         vaccined: false,
#         castrated: false,
#         cat_photos: [
#           'https://instagram.fcgh19-1.fna.fbcdn.net/v/t51.2885-15/275861414_652943802654155_179712488280408818_n.webp?stp=dst-jpg_e35&_nc_ht=instagram.fcgh19-1.fna.fbcdn.net&_nc_cat=111&_nc_ohc=qRRyJysuzX8AX_FikSx&edm=AABBvjUBAAAA&ccb=7-4&ig_cache_key=Mjc5NDAwMTk5NTc0Njk2MDQxMg%3D%3D.2-ccb7-4&oh=00_AT9H2DROvqPWS9YFtt0N1f8JDVR2ea1mf_znRyGXXA4uvQ&oe=62587F1D&_nc_sid=83d603'
#         ]
#       }
#     ]
#   }
# ]
