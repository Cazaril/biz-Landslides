# Introduction to Business API ecosystem

.fx: cover

@conwet

---

# Final steps

The Business API Ecosystem, allows to upload some product attachments
and assets to be sold. These assets are uploaded by the Charging Backend
that saves them in the file system, jointly with the generated PDF
invoices.

In this regard, the directories *src/medi*a and *src/media/bills* must
exists within the Charging Backend directory, and must be writable by
the user executing the Charging Backend.

    !bash
    $ mkdir src/media
    $ mkdir src/media/bills
    $ chown -R <your_user>:<your_user> src/media

---

.fx: back-cover

Thanks!

FIWARE                                FIWARE Lab
OPEN APIs FOR OPEN MINDS              Spark your imagination

         www.fiware.org               FIWARE Ops
twitter: @Fiware                      Easing your operations
