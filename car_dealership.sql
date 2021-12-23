CREATE TABLE "client" (
  "id" SERIAL PRIMARY KEY,
  "full_name" varchar NOT NULL,
  "birthdate" date NOT NULL,
  "phone_number" int,
  "address" varchar NOT NULL
);

CREATE TABLE "brand" (
  "id" SERIAL PRIMARY KEY,
  "name" varchar NOT NULL
);

CREATE TABLE "car" (
  "id" SERIAL PRIMARY KEY,
  "id_brand" int NOT NULL,
  "id_client" int,
  "name" varchar NOT NULL,
  "new" boolean NOT NULL DEFAULT true,
  "doors" int NOT NULL DEFAULT 3,
  "cubic_capacity" int NOT NULL,
  "power" int NOT NULL
);

ALTER TABLE "car" ADD FOREIGN KEY ("id_brand") REFERENCES "brand" ("id");

ALTER TABLE "car" ADD FOREIGN KEY ("id_client") REFERENCES "client" ("id");
