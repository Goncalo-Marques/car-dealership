CREATE TABLE "client" (
  "id" SERIAL PRIMARY KEY,
  "full_name" varchar NOT NULL,
  "birthdate" date NOT NULL,
  "phone_number" int,
  "address" varchar NOT NULL
);

CREATE TABLE "brand" (
  "name" varchar PRIMARY KEY
);

CREATE TABLE "car" (
  "id" SERIAL PRIMARY KEY,
  "brand" varchar NOT NULL,
  "id_client" int DEFAULT null,
  "name" varchar NOT NULL,
  "new" boolean NOT NULL DEFAULT true,
  "doors" int NOT NULL DEFAULT 3,
  "cubic_capacity" int NOT NULL,
  "power" int NOT NULL
);

ALTER TABLE "car" ADD FOREIGN KEY ("brand") REFERENCES "brand" ("name") ON DELETE CASCADE ON UPDATE CASCADE;

ALTER TABLE "car" ADD FOREIGN KEY ("id_client") REFERENCES "client" ("id") ON DELETE SET DEFAULT ON UPDATE NO ACTION;
