PGDMP     0    0                z            MediadToronjas    14.5    14.4 	    ?           0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                      false            ?           0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                      false            ?           0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                      false            ?           1262    24576    MediadToronjas    DATABASE     [   CREATE DATABASE "MediadToronjas" WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE = 'C';
     DROP DATABASE "MediadToronjas";
                postgres    false            ?            1259    24581 	   Productos    TABLE     ?   CREATE TABLE public."Productos" (
    ref integer NOT NULL,
    nombre character varying NOT NULL,
    precio numeric NOT NULL,
    categoria character varying,
    modelo character varying,
    talla numeric NOT NULL,
    color character varying
);
    DROP TABLE public."Productos";
       public         heap    postgres    false            ?            1259    24580    Productos_ref_seq    SEQUENCE     ?   ALTER TABLE public."Productos" ALTER COLUMN ref ADD GENERATED ALWAYS AS IDENTITY (
    SEQUENCE NAME public."Productos_ref_seq"
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);
            public          postgres    false    210            ?          0    24581 	   Productos 
   TABLE DATA           [   COPY public."Productos" (ref, nombre, precio, categoria, modelo, talla, color) FROM stdin;
    public          postgres    false    210   8	       ?           0    0    Productos_ref_seq    SEQUENCE SET     A   SELECT pg_catalog.setval('public."Productos_ref_seq"', 2, true);
          public          postgres    false    209            ]           2606    24587    Productos Productos_pkey 
   CONSTRAINT     [   ALTER TABLE ONLY public."Productos"
    ADD CONSTRAINT "Productos_pkey" PRIMARY KEY (ref);
 F   ALTER TABLE ONLY public."Productos" DROP CONSTRAINT "Productos_pkey";
       public            postgres    false    210            ?   8   x?3???N?????0500???,N????/?M??41?t-.I?-HL??????? ]??     