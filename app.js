/* ================= CONFIG ================= */
const CONFIG = {
  brand: "Tabac Luxe",
  whatsapp: "35228777996",
  email: "info@tabacluxe.lu",
  phone: "+352 28 77 79 96",
  address: "Route de Longwy 549, L-4832, Luxembourg",
  supaUrl: "https://ujmblinyxfjvpntfkohz.supabase.co",
  supaKey: "sb_publishable_O65H3nPdVW5tA-ZZ7HoiVw_gI9M-iDr",
  adminPass: "luxe-admin",
  pdfPath: "https://ujmblinyxfjvpntfkohz.supabase.co/storage/v1/object/public/site-assets/assets/Tabac-Luxe-Liste-de-prix.pdf"
};

/* ================= I18N ================= */
const I18N = {
fr:{
 "nav.home":"Accueil","nav.catalogue":"Catalogue","nav.promos":"Promotions","nav.pricelist":"Liste de prix","nav.contact":"Contact","nav.cart":"Panier",
 "hero.kicker":"Luxembourg — Depuis la frontière, l'excellence",
 "hero.title":"Tabac <em>Luxe</em>",
 "hero.sub":"Tabacs, cigares, shisha et spiritueux d'exception aux meilleurs prix du Grand-Duché. Plus de 500 références, conseil expert, accueil en cinq langues.",
 "hero.cta1":"Découvrir le catalogue","hero.cta2":"Liste de prix complète",
 "sec.cats.k":"Nos univers","sec.cats.t":"Huit univers d'exception",
 "sec.feat.k":"Sélection","sec.feat.t":"Nos incontournables",
 "sec.promo.k":"Bonnes affaires","sec.promo.t":"Promotions en cours",
 "sec.house.k":"La maison","sec.house.t":"Une boutique, une passion",
 "house.p1":"À deux pas de la frontière, Tabac Luxe réunit sous un même toit l'un des plus vastes assortiments de tabacs, cigares, tabacs à rouler, shisha et spiritueux du Luxembourg.",
 "house.p2":"Notre équipe vous conseille en français, allemand, anglais, portugais et luxembourgeois. Tous nos prix sont affichés en toute transparence — la liste complète est téléchargeable librement.",
 "stat.ref":"références en stock","stat.lang":"langues parlées","stat.cats":"univers produits","stat.days":"jours d'ouverture",
 "info.visit":"Nous trouver","info.hours":"Horaires d'ouverture","info.contact":"Contact direct",
 "info.p":"Parking gratuit devant la boutique. Commande WhatsApp : préparez votre panier, envoyez-le nous, retirez-le en magasin.",
 "hours.monfri":"Lundi – Vendredi","hours.sat":"Samedi","hours.sun":"Dimanche","hours.closed":"Fermé","hours.open":"Ouvert maintenant",
 "cat.seau":"Seaux de tabac","cat.pot":"Pots de tabac","cat.potvol":"Pots grand volume","cat.pipe":"Tabac à pipe","cat.rouler":"Tabac à rouler","cat.shisha":"Tabac à chicha","cat.cigares":"Cigares","cat.cigarettes":"Cigarettes",
 "cat.bieres":"Bières","cat.whisky":"Whisky","cat.rhum":"Rhum","cat.vodka":"Vodka","cat.gin":"Gin","cat.anises":"Anisés","cat.energie":"Énergisants","cat.softs":"Softs",
 "card.add":"Ajouter","card.ask":"Prix via WhatsApp","card.featured":"Sélection","card.deal":"Promo","card.new":"Nouveau",
 "cart.title":"Votre panier","cart.empty":"Votre panier est vide.","cart.browse":"Parcourir le catalogue","cart.total":"Total","cart.order":"Commander via WhatsApp","cart.note":"Aucun paiement en ligne — retrait et règlement en magasin uniquement.",
 "pl.title":"Liste de prix complète","pl.sub":"L'intégralité de nos 503 références, prix boutique en EUR et GBP. Téléchargeable en PDF, mise à jour régulièrement.",
 "pl.search":"Rechercher un produit…","pl.allcats":"Toutes les catégories","pl.dl":"Télécharger le PDF","pl.col.p":"Produit","pl.col.eur":"Prix €","pl.col.gbp":"Prix £","pl.col.unit":"Prix au kilo/pièce",
 "pl.note":"Cette liste est générée depuis notre système et reflète les prix à la date indiquée. En cas d'évolution des livraisons ou des taxes, le prix en magasin fait foi. Tabac Luxe s'efforce de maintenir tous les prix à jour.",
 "promo.until":"Dans la limite du stock disponible",
 "contact.title":"Contact & accès","contact.name":"Nom","contact.msg":"Message","contact.send":"Envoyer via WhatsApp",
 "contact.map":"Ouvrir dans Google Maps",
 "footer.tag":"Boutique premium de tabacs, cigares, shisha et spiritueux au Luxembourg.",
 "footer.age":" Vente réservée aux adultes.",
 "footer.visit":"Adresse","footer.hours":"Horaires","footer.links":"Informations",
 "footer.terms":"Conditions générales","footer.privacy":"Politique de confidentialité","footer.disclaimer":"Avertissement légal","footer.notice":"Mentions légales","footer.admin":"Administration",
 "footer.legal":"Vente de tabac et d'alcool réservée aux personnes majeures (18+). Aucune vente en ligne ni expédition : ce site est une vitrine, tout achat s'effectue exclusivement en magasin. L'abus d'alcool est dangereux pour la santé, à consommer avec modération. Fumer tue.",
 "footer.rights":"Tous droits réservés.",
 "age.title":"Accès réservé","age.txt":"Ce site présente des produits du tabac et de l'alcool. Vous devez avoir 18 ans ou plus pour y accéder.","age.yes":"J'ai 18 ans ou plus","age.no":"J'ai moins de 18 ans","age.sorry":"Désolé, l'accès est réservé aux adultes.",
 "toast.added":"ajouté au panier","wa.hello":"Bonjour Tabac Luxe, je souhaite commander :","wa.total":"Total estimé","wa.pickup":"Je passerai retirer et payer en magasin. Merci !",
 "admin.login":"Espace administrateur","admin.pass":"Mot de passe","admin.enter":"Entrer","admin.logout":"Déconnexion",
 "admin.products":"Produits","admin.promos":"Promotions","admin.save":"Enregistrer","admin.saved":"Enregistré ✓","admin.addpromo":"Nouvelle promotion","admin.del":"Supprimer","admin.search":"Filtrer…",
 "admin.hint":"Les modifications sont appliquées immédiatement au site (Supabase).",
 "legal.title.terms":"Conditions Générales de Vente","legal.title.privacy":"Politique de Confidentialité","legal.title.disclaimer":"Avertissement Légal","legal.title.notice":"Mentions Légales"
},
de:{
 "nav.home":"Start","nav.catalogue":"Katalog","nav.promos":"Angebote","nav.pricelist":"Preisliste","nav.contact":"Kontakt","nav.cart":"Warenkorb",
 "hero.kicker":"Luxemburg",
 "hero.title":"Tabac <em>Luxe</em>",
 "hero.sub":"Tabak, Zigarren, Shisha und erlesene Spirituosen zu den besten Preisen des Großherzogtums. Über 500 Artikel, Fachberatung, Service in fünf Sprachen.",
 "hero.cta1":"Katalog entdecken","hero.cta2":"Komplette Preisliste",
 "sec.cats.k":"Unsere Welten","sec.cats.t":"Acht erlesene Welten",
 "sec.feat.k":"Auswahl","sec.feat.t":"Unsere Favoriten",
 "sec.promo.k":"Schnäppchen","sec.promo.t":"Aktuelle Angebote",
 "sec.house.k":"Das Haus","sec.house.t":"Ein Geschäft, eine Leidenschaft",
 "house.p1":"Unweit der Grenze, vereint Tabac Luxe eines der größten Sortimente an Tabak, Zigarren, Drehtabak, Shisha und Spirituosen in Luxemburg.",
 "house.p2":"Wir beraten auf Französisch, Deutsch, Englisch, Portugiesisch und Luxemburgisch. Alle Preise sind transparent — die komplette Liste steht frei zum Download.",
 "stat.ref":"Artikel auf Lager","stat.lang":"gesprochene Sprachen","stat.cats":"Produktwelten","stat.days":"Öffnungstage",
 "info.visit":"Anfahrt","info.hours":"Öffnungszeiten","info.contact":"Direkter Kontakt",
 "info.p":"Kostenlose Parkplätze vor dem Geschäft. WhatsApp-Bestellung: Warenkorb senden, im Geschäft abholen.",
 "hours.monfri":"Montag – Freitag","hours.sat":"Samstag","hours.sun":"Sonntag","hours.closed":"Geschlossen","hours.open":"Jetzt geöffnet",
 "cat.seau":"Tabakeimer","cat.pot":"Tabakdosen","cat.potvol":"Großvolumen-Dosen","cat.pipe":"Pfeifentabak","cat.rouler":"Drehtabak","cat.shisha":"Shisha-Tabak","cat.cigares":"Zigarren","cat.cigarettes":"Zigaretten",
 "cat.bieres":"Biere","cat.whisky":"Whisky","cat.rhum":"Rum","cat.vodka":"Wodka","cat.gin":"Gin","cat.anises":"Anis","cat.energie":"Energydrinks","cat.softs":"Softdrinks",
 "card.add":"Hinzufügen","card.ask":"Preis via WhatsApp","card.featured":"Auswahl","card.deal":"Angebot","card.new":"Neu",
 "cart.title":"Ihr Warenkorb","cart.empty":"Ihr Warenkorb ist leer.","cart.browse":"Katalog durchsuchen","cart.total":"Gesamt","cart.order":"Via WhatsApp bestellen","cart.note":"Kein Online-Verkauf — Abholung und Zahlung nur im Geschäft.",
 "pl.title":"Komplette Preisliste","pl.sub":"Alle 503 Artikel, Ladenpreise in EUR und GBP. Als PDF herunterladbar, regelmäßig aktualisiert.",
 "pl.search":"Produkt suchen…","pl.allcats":"Alle Kategorien","pl.dl":"PDF herunterladen","pl.col.p":"Produkt","pl.col.eur":"Preis €","pl.col.gbp":"Preis £","pl.col.unit":"Preis pro kg/Stück",
 "pl.note":"Diese Liste wird aus unserem System generiert. Bei Änderungen von Lieferungen oder Steuern gilt der Ladenpreis. Tabac Luxe bemüht sich, alle Preise aktuell zu halten.",
 "promo.until":"Solange der Vorrat reicht",
 "contact.title":"Kontakt & Anfahrt","contact.name":"Name","contact.msg":"Nachricht","contact.send":"Via WhatsApp senden",
 "contact.map":"In Google Maps öffnen",
 "footer.tag":"Premium-Geschäft für Tabak, Zigarren, Shisha und Spirituosen in Luxemburg.",
 "footer.age":" Verkauf nur an Erwachsene.",
 "footer.visit":"Adresse","footer.hours":"Öffnungszeiten","footer.links":"Informationen",
 "footer.terms":"AGB","footer.privacy":"Datenschutz","footer.disclaimer":"Haftungsausschluss","footer.notice":"Impressum","footer.admin":"Verwaltung",
 "footer.legal":"Verkauf von Tabak und Alkohol nur an Volljährige (18+). Kein Online-Verkauf und kein Versand: Diese Website ist ein Schaufenster, Käufe erfolgen ausschließlich im Geschäft. Rauchen ist tödlich. Alkohol in Maßen genießen.",
 "footer.rights":"Alle Rechte vorbehalten.",
 "age.title":"Zugang beschränkt","age.txt":"Diese Website zeigt Tabak- und Alkoholprodukte. Zutritt nur ab 18 Jahren.","age.yes":"Ich bin 18 oder älter","age.no":"Ich bin unter 18","age.sorry":"Der Zugang ist Erwachsenen vorbehalten.",
 "toast.added":"zum Warenkorb hinzugefügt","wa.hello":"Hallo Tabac Luxe, ich möchte bestellen:","wa.total":"Voraussichtliche Summe","wa.pickup":"Ich hole die Bestellung im Geschäft ab und zahle vor Ort. Danke!",
 "admin.login":"Adminbereich","admin.pass":"Passwort","admin.enter":"Anmelden","admin.logout":"Abmelden",
 "admin.products":"Produkte","admin.promos":"Angebote","admin.save":"Speichern","admin.saved":"Gespeichert ✓","admin.addpromo":"Neues Angebot","admin.del":"Löschen","admin.search":"Filtern…",
 "admin.hint":"Änderungen werden sofort auf der Website wirksam (Supabase).",
 "legal.title.terms":"Allgemeine Geschäftsbedingungen","legal.title.privacy":"Datenschutzerklärung","legal.title.disclaimer":"Haftungsausschluss","legal.title.notice":"Impressum"
},
en:{
 "nav.home":"Home","nav.catalogue":"Catalogue","nav.promos":"Deals","nav.pricelist":"Price list","nav.contact":"Contact","nav.cart":"Cart",
 "hero.kicker":"Luxembourg",
 "hero.title":"Tabac <em>Luxe</em>",
 "hero.sub":"Tobacco, cigars, shisha and fine spirits at the Grand Duchy's sharpest prices. Over 500 references, expert advice, welcome in five languages.",
 "hero.cta1":"Explore the catalogue","hero.cta2":"Full price list",
 "sec.cats.k":"Our worlds","sec.cats.t":"Eight worlds of exception",
 "sec.feat.k":"Selection","sec.feat.t":"Our essentials",
 "sec.promo.k":"Good deals","sec.promo.t":"Current promotions",
 "sec.house.k":"The house","sec.house.t":"One shop, one passion",
 "house.p1":"A stone's throw from the border, Tabac Luxe brings together one of Luxembourg's largest ranges of tobacco, cigars, rolling tobacco, shisha and spirits.",
 "house.p2":"Our team advises you in French, German, English, Portuguese and Luxembourgish. All prices are fully transparent — the complete list is free to download.",
 "stat.ref":"references in stock","stat.lang":"languages spoken","stat.cats":"product worlds","stat.days":"opening days",
 "info.visit":"Find us","info.hours":"Opening hours","info.contact":"Direct contact",
 "info.p":"Free parking in front of the shop. WhatsApp ordering: build your cart, send it to us, collect in store.",
 "hours.monfri":"Monday – Friday","hours.sat":"Saturday","hours.sun":"Sunday","hours.closed":"Closed","hours.open":"Open now",
 "cat.seau":"Tobacco buckets","cat.pot":"Tobacco tins","cat.potvol":"High-volume tins","cat.pipe":"Pipe tobacco","cat.rouler":"Rolling tobacco","cat.shisha":"Shisha tobacco","cat.cigares":"Cigars","cat.cigarettes":"Cigarettes",
 "cat.bieres":"Beers","cat.whisky":"Whisky","cat.rhum":"Rum","cat.vodka":"Vodka","cat.gin":"Gin","cat.anises":"Aniseed","cat.energie":"Energy drinks","cat.softs":"Soft drinks",
 "card.add":"Add","card.ask":"Price via WhatsApp","card.featured":"Featured","card.deal":"Deal","card.new":"New",
 "cart.title":"Your cart","cart.empty":"Your cart is empty.","cart.browse":"Browse the catalogue","cart.total":"Total","cart.order":"Order via WhatsApp","cart.note":"No online payment — collection and payment in store only.",
 "pl.title":"Complete price list","pl.sub":"All 503 references, in-store prices in EUR and GBP. Downloadable as PDF, updated regularly.",
 "pl.search":"Search a product…","pl.allcats":"All categories","pl.dl":"Download PDF","pl.col.p":"Product","pl.col.eur":"Price €","pl.col.gbp":"Price £","pl.col.unit":"Price per kg/piece",
 "pl.note":"This list is generated from our system and reflects prices at the date shown. In exceptional cases (deliveries, taxes), the in-store price prevails. Tabac Luxe strives to keep all prices up to date.",
 "promo.until":"While stocks last",
 "contact.title":"Contact & directions","contact.name":"Name","contact.msg":"Message","contact.send":"Send via WhatsApp",
 "contact.map":"Open in Google Maps",
 "footer.tag":"Premium tobacco, cigars, shisha and spirits boutique in Luxembourg.",
 "footer.age":" Adults only.",
 "footer.visit":"Address","footer.hours":"Hours","footer.links":"Information",
 "footer.terms":"Terms & Conditions","footer.privacy":"Privacy Policy","footer.disclaimer":"Disclaimer","footer.notice":"Legal notice","footer.admin":"Admin",
 "footer.legal":"Sale of tobacco and alcohol restricted to adults (18+). No online sales or shipping: this website is a showcase — all purchases are made exclusively in store. Smoking kills. Enjoy alcohol responsibly.",
 "footer.rights":"All rights reserved.",
 "age.title":"Restricted access","age.txt":"This site displays tobacco and alcohol products. You must be 18 or older to enter.","age.yes":"I am 18 or older","age.no":"I am under 18","age.sorry":"Sorry, access is restricted to adults.",
 "toast.added":"added to cart","wa.hello":"Hello Tabac Luxe, I would like to order:","wa.total":"Estimated total","wa.pickup":"I will collect and pay in store. Thank you!",
 "admin.login":"Admin area","admin.pass":"Password","admin.enter":"Sign in","admin.logout":"Sign out",
 "admin.products":"Products","admin.promos":"Promotions","admin.save":"Save","admin.saved":"Saved ✓","admin.addpromo":"New promotion","admin.del":"Delete","admin.search":"Filter…",
 "admin.hint":"Changes go live on the site immediately (Supabase).",
 "legal.title.terms":"Terms & Conditions","legal.title.privacy":"Privacy Policy","legal.title.disclaimer":"Disclaimer","legal.title.notice":"Legal Notice"
},
pt:{
 "nav.home":"Início","nav.catalogue":"Catálogo","nav.promos":"Promoções","nav.pricelist":"Lista de preços","nav.contact":"Contacto","nav.cart":"Carrinho",
 "hero.kicker":"Luxemburgo",
 "hero.title":"Tabac <em>Luxe</em>",
 "hero.sub":"Tabaco, charutos, shisha e bebidas espirituosas aos melhores preços do Grão-Ducado. Mais de 500 referências, aconselhamento especializado, atendimento em cinco línguas.",
 "hero.cta1":"Explorar o catálogo","hero.cta2":"Lista de preços completa",
 "sec.cats.k":"Os nossos mundos","sec.cats.t":"Oito mundos de exceção",
 "sec.feat.k":"Seleção","sec.feat.t":"Os nossos essenciais",
 "sec.promo.k":"Boas ofertas","sec.promo.t":"Promoções em curso",
 "sec.house.k":"A casa","sec.house.t":"Uma loja, uma paixão",
 "house.p1":"A dois passos da fronteira, o Tabac Luxe reúne um dos maiores sortimentos de tabaco, charutos, tabaco de enrolar, shisha e bebidas do Luxemburgo.",
 "house.p2":"Aconselhamos em francês, alemão, inglês, português e luxemburguês. Todos os preços são transparentes — a lista completa está disponível para descarregar.",
 "stat.ref":"referências em stock","stat.lang":"línguas faladas","stat.cats":"mundos de produtos","stat.days":"dias de abertura",
 "info.visit":"Como chegar","info.hours":"Horário de abertura","info.contact":"Contacto direto",
 "info.p":"Estacionamento gratuito em frente à loja. Encomenda por WhatsApp: monte o carrinho, envie-nos e levante na loja.",
 "hours.monfri":"Segunda – Sexta","hours.sat":"Sábado","hours.sun":"Domingo","hours.closed":"Fechado","hours.open":"Aberto agora",
 "cat.seau":"Baldes de tabaco","cat.pot":"Latas de tabaco","cat.potvol":"Latas grande volume","cat.pipe":"Tabaco de cachimbo","cat.rouler":"Tabaco de enrolar","cat.shisha":"Tabaco de shisha","cat.cigares":"Charutos","cat.cigarettes":"Cigarros",
 "cat.bieres":"Cervejas","cat.whisky":"Whisky","cat.rhum":"Rum","cat.vodka":"Vodka","cat.gin":"Gin","cat.anises":"Anisados","cat.energie":"Energéticos","cat.softs":"Refrigerantes",
 "card.add":"Adicionar","card.ask":"Preço via WhatsApp","card.featured":"Seleção","card.deal":"Promoção","card.new":"Novo",
 "cart.title":"O seu carrinho","cart.empty":"O seu carrinho está vazio.","cart.browse":"Ver o catálogo","cart.total":"Total","cart.order":"Encomendar via WhatsApp","cart.note":"Sem pagamento online — levantamento e pagamento apenas na loja.",
 "pl.title":"Lista de preços completa","pl.sub":"Todas as 503 referências, preços de loja em EUR e GBP. Descarregável em PDF, atualizada regularmente.",
 "pl.search":"Procurar produto…","pl.allcats":"Todas as categorias","pl.dl":"Descarregar PDF","pl.col.p":"Produto","pl.col.eur":"Preço €","pl.col.gbp":"Preço £","pl.col.unit":"Preço por kg/peça",
 "pl.note":"Esta lista é gerada a partir do nosso sistema e reflete os preços à data indicada. Em casos excecionais (entregas, impostos), prevalece o preço em loja. O Tabac Luxe esforça-se por manter os preços atualizados.",
 "promo.until":"Até esgotar o stock",
 "contact.title":"Contacto & acesso","contact.name":"Nome","contact.msg":"Mensagem","contact.send":"Enviar via WhatsApp",
 "contact.map":"Abrir no Google Maps",
 "footer.tag":"Boutique premium de tabaco, charutos, shisha e bebidas no Luxemburgo.",
 "footer.age":" Venda reservada a adultos.",
 "footer.visit":"Morada","footer.hours":"Horário","footer.links":"Informações",
 "footer.terms":"Termos e Condições","footer.privacy":"Política de Privacidade","footer.disclaimer":"Aviso legal","footer.notice":"Menções legais","footer.admin":"Administração",
 "footer.legal":"Venda de tabaco e álcool reservada a maiores de 18 anos. Sem venda online nem envios: este site é uma montra — todas as compras são feitas exclusivamente na loja. Fumar mata. Consuma álcool com moderação.",
 "footer.rights":"Todos os direitos reservados.",
 "age.title":"Acesso restrito","age.txt":"Este site apresenta produtos de tabaco e álcool. Deve ter 18 anos ou mais para aceder.","age.yes":"Tenho 18 anos ou mais","age.no":"Tenho menos de 18 anos","age.sorry":"O acesso é reservado a adultos.",
 "toast.added":"adicionado ao carrinho","wa.hello":"Olá Tabac Luxe, gostaria de encomendar:","wa.total":"Total estimado","wa.pickup":"Vou levantar e pagar na loja. Obrigado!",
 "admin.login":"Área de administração","admin.pass":"Palavra-passe","admin.enter":"Entrar","admin.logout":"Sair",
 "admin.products":"Produtos","admin.promos":"Promoções","admin.save":"Guardar","admin.saved":"Guardado ✓","admin.addpromo":"Nova promoção","admin.del":"Eliminar","admin.search":"Filtrar…",
 "admin.hint":"As alterações entram em vigor imediatamente no site (Supabase).",
 "legal.title.terms":"Termos e Condições","legal.title.privacy":"Política de Privacidade","legal.title.disclaimer":"Aviso Legal","legal.title.notice":"Menções Legais"
},
lb:{
 "nav.home":"Heem","nav.catalogue":"Katalog","nav.promos":"Promotiounen","nav.pricelist":"Präislëscht","nav.contact":"Kontakt","nav.cart":"Weekuerf",
 "hero.kicker":"Lëtzebuerg",
 "hero.title":"Tabac <em>Luxe</em>",
 "hero.sub":"Tabak, Zigarren, Shisha a feine Séiwäin zu de beschte Präisser am Groussherzogtum. Iwwer 500 Artikelen, fachkonnege Rot, Service a fënnef Sproochen.",
 "hero.cta1":"Katalog entdecken","hero.cta2":"Komplett Präislëscht",
 "sec.cats.k":"Eis Welten","sec.cats.t":"Aacht erles Welten",
 "sec.feat.k":"Auswiel","sec.feat.t":"Eis Favoritten",
 "sec.promo.k":"Gutt Offeren","sec.promo.t":"Aktuell Promotiounen",
 "sec.house.k":"Den Haus","sec.house.t":"E Geschäft, eng Leidenschaft",
 "house.p1":"No bei der Grenz, vereent de Tabac Luxe eent vun de gréisste Sortimenter un Tabak, Zigarren, Dréhtabak, Shisha a Séiwäin zu Lëtzebuerg.",
 "house.p2":"Mir beroden op Franséisch, Däitsch, Englesch, Portugisesch a Lëtzebuergesch. All Präisser sinn transparent — déi komplett Lëscht ass fräi erofzelueden.",
 "stat.ref":"Artikelen op Stock","stat.lang":"Sproochen","stat.cats":"Produktwelten","stat.days":"Opmaachungsdeeg",
 "info.visit":"Eis fannen","info.hours":"Opmaachungszäiten","info.contact":"Direkte Kontakt",
 "info.p":"Gratis Parking virum Geschäft. WhatsApp-Bestellung: Weekuerf schécken, am Geschäft ophuelen.",
 "hours.monfri":"Méindeg – Freideg","hours.sat":"Samschdeg","hours.sun":"Sonndeg","hours.closed":"Zou","hours.open":"Elo op",
 "cat.seau":"Tabaksemer","cat.pot":"Tabaksdosen","cat.potvol":"Grossvolumen-Dosen","cat.pipe":"Päifetabak","cat.rouler":"Dréhtabak","cat.shisha":"Shisha-Tabak","cat.cigares":"Zigarren","cat.cigarettes":"Zigaretten",
 "cat.bieres":"Bieren","cat.whisky":"Whisky","cat.rhum":"Rum","cat.vodka":"Wodka","cat.gin":"Gin","cat.anises":"Anis","cat.energie":"Energydrénker","cat.softs":"Séftdrénker",
 "card.add":"Derbäi","card.ask":"Präis via WhatsApp","card.featured":"Auswiel","card.deal":"Promo","card.new":"Nei",
 "cart.title":"Äre Weekuerf","cart.empty":"Äre Weekuerf ass eidel.","cart.browse":"Katalog kucken","cart.total":"Total","cart.order":"Via WhatsApp bestellen","cart.note":"Keng Online-Bezuelung — Ophuelung a Bezuelung nëmmen am Geschäft.",
 "pl.title":"Komplett Präislëscht","pl.sub":"All 503 Artikelen, Geschäftspräisser an EUR a GBP. Als PDF erofzelueden, regelméisseg aktualiséiert.",
 "pl.search":"Produkt sichen…","pl.allcats":"All Kategorien","pl.dl":"PDF eroflueden","pl.col.p":"Produkt","pl.col.eur":"Präis €","pl.col.gbp":"Präis £","pl.col.unit":"Präis pro kg/Stéck",
 "pl.note":"Dës Lëscht gëtt aus eisem System generéiert. Bei Änderunge vu Liwwerungen oder Steiere gëlt de Präis am Geschäft. Tabac Luxe beméit sech, all Präisser aktuell ze halen.",
 "promo.until":"Laang de Stock reicht",
 "contact.title":"Kontakt & Uschloss","contact.name":"Numm","contact.msg":"Message","contact.send":"Via WhatsApp schécken",
 "contact.map":"A Google Maps opmaachen",
 "footer.tag":"Premium-Geschäft fir Tabak, Zigarren, Shisha a Séiwäin zu Lëtzebuerg.",
 "footer.age":" Verkaf nëmmen un Erwuessener.",
 "footer.visit":"Adress","footer.hours":"Zäiten","footer.links":"Informatiounen",
 "footer.terms":"Allgemeng Konditiounen","footer.privacy":"Dateschutz","footer.disclaimer":"Haftungsausschloss","footer.notice":"Impressum","footer.admin":"Administratioun",
 "footer.legal":"Verkaf vun Tabak an Alkohol nëmmen un Volljäregen (18+). Kee Online-Verkaf a kee Versand: dës Websäit ass e Schafenster — all Keef ginn exklusiv am Geschäft gemaach. Fëmmen ëmbréngt. Alkohol mat Mooss genéissen.",
 "footer.rights":"All Rechter virbehal.",
 "age.title":"Zougang limitéiert","age.txt":"Dës Websäit weist Tabaks- an Alkoholsprodukter. Zougang eréischt ab 18 Joer.","age.yes":"Ech si 18 oder méi al","age.no":"Ech si méi jonk wéi 18","age.sorry":"Leider ass den Zougang Erwuessene virbehal.",
 "toast.added":"an de Weekuerf geluecht","wa.hello":"Moien Tabac Luxe, ech géif gär bestellen:","wa.total":"Geschaate Total","wa.pickup":"Ech kommen d'Bestellung am Geschäft ophuelen a bezuelen. Merci!",
 "admin.login":"Adminberäich","admin.pass":"Passwuert","admin.enter":"Umellen","admin.logout":"Ofmellen",
 "admin.products":"Produkter","admin.promos":"Promotiounen","admin.save":"Späicheren","admin.saved":"Gespäichert ✓","admin.addpromo":"Nei Promotioun","admin.del":"Läschen","admin.search":"Filteren…",
 "admin.hint":"Änderunge ginn direkt op der Websäit aktiv (Supabase).",
 "legal.title.terms":"Allgemeng Geschäftskonditiounen","legal.title.privacy":"Dateschutzerklärung","legal.title.disclaimer":"Haftungsausschloss","legal.title.notice":"Impressum"
}
};
/* ================= STATE / DATA ================= */
let LANG = localStorage.getItem('tl_lang') || 'fr';
const t = k => (I18N[LANG] && I18N[LANG][k]) || I18N.fr[k] || k;
const eur = n => n==null ? '' : '€' + Number(n).toFixed(2).replace('.',',');
const gbp = n => n==null ? '' : '£' + Number(n).toFixed(2).replace('.',',');
const FORCE_LOGO_SLUGS = new Set(['the-turner-original-50g-rouler']);
const BRAND_LOGOS = {
  agio: 'assets/brand-logos/agio.svg',
  'the turner': 'assets/brand-logos/the-turner.svg'
};
const storageUrl = path => {
  if(!path) return '';
  return /^https?:\/\//i.test(path) ? path : CONFIG.supaUrl + '/storage/v1/object/public/site-assets/' + path.replace(/^\/+/, '');
};
function imgOpt(url,width=360,quality=72){
  if(!url) return '';
  const full = storageUrl(url);
  const marker = '/storage/v1/object/public/site-assets/';
  const idx = full.indexOf(marker);
  if(idx === -1 || full.startsWith('data:')) return full;
  const path = full.slice(idx + marker.length);
  return `${CONFIG.supaUrl}/storage/v1/render/image/public/site-assets/${path}?width=${width}&quality=${quality}`;
}
function imgSet(url, widths=[220,360,540]){
  return widths.map(w => `${imgOpt(url,w)} ${w}w`).join(', ');
}
function brandName(name){
  const words = String(name || 'Tabac Luxe').trim().split(/\s+/).filter(Boolean);
  if(words[0] && words[0].toLowerCase()==='the' && words[1]) return `${words[0]} ${words[1]}`;
  return words[0] || 'Tabac Luxe';
}
function normBrand(s){ return String(s||'').toLowerCase().normalize('NFD').replace(/[\u0300-\u036f]/g,'').replace(/[^a-z0-9]+/g,''); }
function imageMatchesProduct(p){
  if(!p.image || FORCE_LOGO_SLUGS.has(p.slug)) return false;
  return normBrand(p.image).includes(normBrand(brandName(p.name)));
}
function brandLogoSrc(name){
  const brand = brandName(name).slice(0,28);
  const localLogo = BRAND_LOGOS[brand.toLowerCase()];
  if(localLogo) return localLogo;
  const initials = brand.split(/\s+/).map(w=>w[0]).join('').slice(0,3).toUpperCase() || 'TL';
  const svg = `<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 600 600"><rect width="600" height="600" rx="24" fill="#faf8f4"/><rect x="36" y="36" width="528" height="528" rx="18" fill="#fff" stroke="#d9c08a" stroke-width="10"/><text x="300" y="280" font-family="Georgia,serif" font-size="118" font-weight="700" fill="#b08d3e" text-anchor="middle">${initials}</text><text x="300" y="370" font-family="Arial,sans-serif" font-size="44" font-weight="700" fill="#2b2620" text-anchor="middle">${brand.replace(/&/g,'&amp;').replace(/</g,'&lt;')}</text><text x="300" y="430" font-family="Arial,sans-serif" font-size="25" letter-spacing="5" fill="#6d6353" text-anchor="middle">TABAC LUXE</text></svg>`;
  return 'data:image/svg+xml;charset=UTF-8,' + encodeURIComponent(svg);
}

const CAT_ORDER = ['seau','pot','potvol','pipe','rouler','shisha','cigares','cigarettes','bieres','whisky','rhum','vodka','gin','anises','energie','softs'];
const CAT_IMG = {
  seau:'https://ujmblinyxfjvpntfkohz.supabase.co/storage/v1/object/public/site-assets/assets/products/marlboro-bucket.jpg', pot:'https://ujmblinyxfjvpntfkohz.supabase.co/storage/v1/object/public/site-assets/assets/products/pueblo-blue.jpg',
  potvol:'https://ujmblinyxfjvpntfkohz.supabase.co/storage/v1/object/public/site-assets/assets/products/camel-yellow.jpg', pipe:'https://ujmblinyxfjvpntfkohz.supabase.co/storage/v1/object/public/site-assets/assets/products/golden-virginia.jpg',
  rouler:'https://ujmblinyxfjvpntfkohz.supabase.co/storage/v1/object/public/site-assets/assets/products/amber-leaf.jpg', shisha:'https://ujmblinyxfjvpntfkohz.supabase.co/storage/v1/object/public/site-assets/assets/products/adalya-ladykiller.jpg',
  cigares:'https://ujmblinyxfjvpntfkohz.supabase.co/storage/v1/object/public/site-assets/assets/products/cohiba-siglo.jpg', cigarettes:'https://ujmblinyxfjvpntfkohz.supabase.co/storage/v1/object/public/site-assets/assets/products/marlboro.jpg',
  bieres:'https://ujmblinyxfjvpntfkohz.supabase.co/storage/v1/object/public/site-assets/assets/products/corona.jpg', whisky:'https://ujmblinyxfjvpntfkohz.supabase.co/storage/v1/object/public/site-assets/assets/products/chivas.jpg',
  rhum:'https://ujmblinyxfjvpntfkohz.supabase.co/storage/v1/object/public/site-assets/assets/products/bumbu.jpg', vodka:'https://ujmblinyxfjvpntfkohz.supabase.co/storage/v1/object/public/site-assets/assets/products/absolut.jpg',
  gin:'https://ujmblinyxfjvpntfkohz.supabase.co/storage/v1/object/public/site-assets/assets/products/tanqueray.jpg', anises:'https://ujmblinyxfjvpntfkohz.supabase.co/storage/v1/object/public/site-assets/assets/products/ricard.jpg',
  energie:'https://ujmblinyxfjvpntfkohz.supabase.co/storage/v1/object/public/site-assets/assets/products/redbull.jpg', softs:'https://ujmblinyxfjvpntfkohz.supabase.co/storage/v1/object/public/site-assets/assets/products/cocacola.jpg'
};

let DB = { products: [], promos: [], pl: null };
const FEAT = () => DB.products.filter(p=>p.featured && p.active!==false);

async function api(path, opts={}){
  const r = await fetch(CONFIG.supaUrl + '/rest/v1/' + path, {
    ...opts,
    headers: { apikey: CONFIG.supaKey, Authorization: 'Bearer ' + CONFIG.supaKey,
      'Content-Type':'application/json', ...(opts.headers||{}) }
  });
  if(!r.ok) throw new Error(r.status);
  const txt = await r.text();
  return txt ? JSON.parse(txt) : null;
}

async function loadData(){
  try{
    const [prods, promos] = await Promise.all([
      fetch('data/products.json').then(r=>r.json()),
      fetch('data/promos.json').then(r=>r.json())
    ]);
    DB.products = prods; DB.promos = promos;
  }catch(e){
    try{
      const [prods, promos] = await Promise.all([
        api('products?select=*&order=category.asc,name.asc&limit=1200'),
        api('promos?select=*&active=eq.true&order=sort.asc')
      ]);
      DB.products = prods; DB.promos = promos;
    }catch(_e){ DB.products = []; DB.promos = []; }
  }
  try{
    const r = await fetch('data/price_list.json');
    DB.pl = await r.json();
  }catch(e){ DB.pl = null; }
}

/* ================= CART ================= */
let cart = JSON.parse(localStorage.getItem('tl_cart')||'{}');
function saveCart(){ localStorage.setItem('tl_cart', JSON.stringify(cart)); updateCartN(); }
function updateCartN(){ document.getElementById('cartN').textContent = Object.values(cart).reduce((a,b)=>a+b,0); }
function addToCart(slug){
  cart[slug]=(cart[slug]||0)+1; saveCart();
  const p = DB.products.find(x=>x.slug===slug);
  toast((p?p.name:'') + ' ' + t('toast.added'));
}
function setQty(slug,q){ if(q<=0) delete cart[slug]; else cart[slug]=q; saveCart(); render(); }
function cartTotal(){
  return Object.entries(cart).reduce((s,[sl,q])=>{
    const p=DB.products.find(x=>x.slug===sl); return s + (p&&p.price_eur? p.price_eur*q : 0);
  },0);
}
function waCart(){
  const lines = Object.entries(cart).map(([sl,q])=>{
    const p=DB.products.find(x=>x.slug===sl);
    return p ? `• ${q} × ${p.name}${p.price_eur? ' — '+eur(p.price_eur):''}` : '';
  }).filter(Boolean);
  const msg = `${t('wa.hello')}\n\n${lines.join('\n')}\n\n${t('wa.total')}: ${eur(cartTotal())}\n${t('wa.pickup')}`;
  window.open(`https://wa.me/${CONFIG.whatsapp}?text=${encodeURIComponent(msg)}`,'_blank');
}
function waAsk(p){
  const msg = `Bonjour Tabac Luxe, quel est le prix de : ${p.name} ? / Hello, price please: ${p.name}`;
  window.open(`https://wa.me/${CONFIG.whatsapp}?text=${encodeURIComponent(msg)}`,'_blank');
}

/* ================= HELPERS ================= */
function toast(msg){
  const el=document.getElementById('toast'); el.textContent=msg; el.classList.add('show');
  setTimeout(()=>el.classList.remove('show'),2200);
}
function productCard(p){
  const imgUrl = imageMatchesProduct(p) ? storageUrl(p.image) : brandLogoSrc(p.name);
  const logoName = String(p.name || 'Tabac Luxe').replace(/"/g,'&quot;');
  const isData = /^data:/i.test(imgUrl);
  const img = imgUrl ? `<img src="${isData ? imgUrl : imgOpt(imgUrl,360)}" srcset="${isData ? '' : imgSet(imgUrl,[220,360,540])}" sizes="(max-width:560px) 46vw, 213px" width="213" height="213" alt="${p.name} — ${t('cat.'+p.category)||p.category} at Tabac Luxe" data-logo-name="${logoName}" loading="lazy" decoding="async" onerror="this.replaceWith(productLogo(this.dataset.logoName))">` :
    `<div style="font-family:var(--serif);font-size:2.6rem;color:var(--goldlt)">${p.name.split(' ')[0]}</div>`;
  const badge = p.deal? `<span class="pbadge">${t('card.deal')}</span>` : (p.featured? `<span class="pbadge new">${t('card.featured')}</span>`:'');
  const priceHtml = p.price_eur!=null
    ? `<div class="price">${eur(p.price_eur)}${p.unit_price? `<br><small>${eur(p.unit_price)}/${p.unit==='kg'?'kg':'st.'}</small>`:''}</div>
       <button class="add" onclick="addToCart('${p.slug}')">${t('card.add')}</button>`
    : `<div></div><button class="add ask" onclick='waAsk(${JSON.stringify(p)})'>${t('card.ask')}</button>`;
  return `<div class="pcard reveal" onclick="openProduct('${p.slug}',event)" style="cursor:pointer" role="link" tabindex="0" onkeydown="if(event.key==='Enter')openProduct('${p.slug}',event)">${badge}<div class="pimg">${img}</div>
    <div class="pbody"><div class="pcat">${t('cat.'+p.category)||p.category}</div>
    <div class="pname">${p.name}</div>
    <div class="pfoot">${priceHtml}</div></div></div>`;
}
function openProduct(slug,ev){
  if(ev && ev.target.closest('button.add')) return; // let the Add-to-cart button work
  window.location.href='product/'+encodeURIComponent(slug)+'.html';
}
function productLogo(name){
  const el=document.createElement('div');
  el.style.cssText='font-family:var(--serif);font-size:2rem;color:var(--gold);text-align:center;line-height:1.1;padding:.5rem';
  el.textContent=(name||'Tabac Luxe').split(' ').slice(0,2).join(' ');
  return el;
}
function revealInit(){
  document.querySelectorAll('.reveal:not(.vis)').forEach(el=>el.classList.add('vis'));
}

/* ================= VIEWS ================= */
function homeHeroHtml(){
  return `
  <section class="hero" style="padding:0">
    <div class="shade"></div>
    <div class="inner">
      <div class="kicker">${t('hero.kicker')}</div>
      <h1>${t('hero.title')}</h1>
      <div class="rule"></div>
      <p>${t('hero.sub')}</p>
      <div class="btnrow">
        <a class="btn" href="#/catalogue">${t('hero.cta1')}</a>
        <a class="btn ghost" href="#/tarifs">${t('hero.cta2')}</a>
      </div>
    </div>
  </section>`;
}
function homeBelowHtml(){
  const catsHtml = CAT_ORDER.slice(0,8).map(c=>{
    const n = DB.products.filter(p=>p.category===c).length;
    return `<div class="cat reveal" onclick="location.hash='#/catalogue/${c}'">
      <div class="ci"><img src="${imgOpt(CAT_IMG[c],180,65)}" srcset="${imgSet(CAT_IMG[c],[140,180,260])}" sizes="130px" width="130" height="110" alt="${t('cat.'+c)}" loading="lazy" decoding="async"></div>
      <h3>${t('cat.'+c)}</h3><div class="n">${n} ${LANG==='fr'?'références':LANG==='de'?'Artikel':LANG==='pt'?'referências':LANG==='lb'?'Artikelen':'references'}</div></div>`;
  }).join('');
  const feat = FEAT().slice(0,8).map(productCard).join('');
  const promos = DB.promos.slice(0,3).map(pr=>`
    <div class="promo reveal"><span class="badge">${pr.badge||'Promo'}</span>
    <h3>${(pr.title&&pr.title[LANG])||(pr.title&&pr.title.fr)||''}</h3>
    <p>${(pr.body&&pr.body[LANG])||(pr.body&&pr.body.fr)||''}</p>
    <p style="font-size:.68rem;letter-spacing:.2em;text-transform:uppercase;color:var(--goldlt)">${t('promo.until')}</p></div>`).join('');
  return `
  <section><div class="wrap">
    <div class="sec-head reveal"><div class="kicker">${t('sec.cats.k')}</div><h2>${t('sec.cats.t')}</h2><div class="rule"></div></div>
    <div class="cats">${catsHtml}</div>
  </div></section>

  <section class="alt"><div class="wrap">
    <div class="sec-head reveal"><div class="kicker">${t('sec.feat.k')}</div><h2>${t('sec.feat.t')}</h2><div class="rule"></div></div>
    <div class="caro">${feat}</div>
  </div></section>

  <section style="padding:0">
    <div class="split">
      <div class="img" style="background-image:url('${imgOpt('assets/hero/cigars.jpg',760,65)}')"></div>
      <div class="txt reveal">
        <div class="kicker">${t('sec.house.k')}</div>
        <h2>${t('sec.house.t')}</h2>
        <p>${t('house.p1')}</p><p>${t('house.p2')}</p>
        <div class="stats">
          <div class="stat"><b>503</b><span>${t('stat.ref')}</span></div>
          <div class="stat"><b>5</b><span>${t('stat.lang')}</span></div>
          <div class="stat"><b>8</b><span>${t('stat.cats')}</span></div>
          <div class="stat"><b>6</b><span>${t('stat.days')}</span></div>
        </div>
      </div>
    </div>
  </section>

  ${promos? `<section class="alt"><div class="wrap">
    <div class="sec-head reveal"><div class="kicker">${t('sec.promo.k')}</div><h2>${t('sec.promo.t')}</h2><div class="rule"></div></div>
    <div class="promos">${promos}</div>
  </div></section>`:''}

  <section class="info"><div class="wrap">
    <div class="cols">
      <div class="reveal"><h3>${t('info.visit')}</h3>
        <p>${CONFIG.address}</p><p style="margin-top:.8rem">${t('info.p')}</p></div>
      <div class="reveal"><h3>${t('info.hours')}</h3>
        <ul>
          <li><span>${t('hours.monfri')}</span><b>06:00 – 18:00</b></li>
          <li><span>${t('hours.sat')}</span><b>08:00 – 17:00</b></li>
          <li><span>${t('hours.sun')}</span><b class="closed">${t('hours.closed')}</b></li>
        </ul></div>
      <div class="reveal"><h3>${t('info.contact')}</h3>
        <p><a href="mailto:${CONFIG.email}" style="color:#efe7d6">${CONFIG.email}</a><br>
        <a href="tel:+35228777996" style="color:#efe7d6">${CONFIG.phone}</a></p>
        <p style="margin-top:.8rem"><a class="btn" style="border-color:var(--gold2);background:var(--gold2)" href="https://wa.me/${CONFIG.whatsapp}" target="_blank" rel="noopener">WhatsApp</a></p></div>
    </div>
  </div></section>`;
}
function viewHome(){
  const defer = !window.__homeBelowLoaded;
  if(defer){
    setTimeout(async ()=>{
      await loadData();
      window.__homeBelowLoaded = true;
      const el = document.getElementById('homeDeferred');
      if(el){ el.innerHTML = homeBelowHtml(); revealInit(); }
    }, 7000);
    return homeHeroHtml() + '<div id="homeDeferred" aria-live="polite"></div>';
  }
  return homeHeroHtml() + homeBelowHtml();
}

function viewCatalogue(cat){
  const cats = CAT_ORDER.map(c=>`<option value="${c}" ${c===cat?'selected':''}>${t('cat.'+c)}</option>`).join('');
  return `<section><div class="wrap">
    <div class="sec-head"><div class="kicker">Tabac Luxe</div><h2>${t('nav.catalogue')}</h2><div class="rule"></div></div>
    <div class="pl-tools">
      <input id="q" placeholder="${t('pl.search')}" oninput="catFilter()">
      <select id="cat" onchange="catFilter()"><option value="">${t('pl.allcats')}</option>${cats}</select>
    </div>
    <div class="grid" id="catGrid"></div>
  </div></section>
  <script>setTimeout(catFilter,0)<\/script>`;
}
window.catFilter = function(){
  const q=(document.getElementById('q').value||'').toLowerCase();
  const c=document.getElementById('cat').value;
  const list=DB.products.filter(p=>(p.active!==false) && (p.image||p.price_eur!=null) &&
    (!c||p.category===c) && (!q||p.name.toLowerCase().includes(q)));
  const withImg=list.filter(p=>p.image), noImg=list.filter(p=>!p.image);
  document.getElementById('catGrid').innerHTML=[...withImg,...noImg].slice(0,120).map(productCard).join('') ||
    `<p style="grid-column:1/-1;text-align:center;color:var(--ink2)">—</p>`;
  revealInit();
};

function viewPromos(){
  const list = DB.promos.map(pr=>`
    <div class="promo reveal"><span class="badge">${pr.badge||'Promo'}</span>
    <h3>${(pr.title&&pr.title[LANG])||(pr.title&&pr.title.fr)||''}</h3>
    <p>${(pr.body&&pr.body[LANG])||(pr.body&&pr.body.fr)||''}</p>
    <p style="font-size:.68rem;letter-spacing:.2em;text-transform:uppercase;color:var(--goldlt)">${t('promo.until')}</p></div>`).join('');
  return `<section><div class="wrap">
    <div class="sec-head"><div class="kicker">Tabac Luxe</div><h2>${t('nav.promos')}</h2><div class="rule"></div></div>
    <div class="promos">${list || `<p style="color:var(--ink2)">—</p>`}</div>
  </div></section>`;
}

function viewPriceList(){
  const catNames = {seau:t('cat.seau'),pot:t('cat.pot'),potvol:t('cat.potvol'),pipe:t('cat.pipe'),rouler:t('cat.rouler'),shisha:t('cat.shisha'),cigares:t('cat.cigares'),cigarettes:t('cat.cigarettes')};
  let cats = [];
  if (DB.pl) cats = DB.pl.map(c=>({key:cat_key(c.en), items:c.items}));
  else cats = CAT_ORDER.slice(0,8).map(k=>({key:k, items:DB.products.filter(p=>p.category===k).map(p=>({name:p.name,eur:p.price_eur,gbp:p.price_gbp,unit_price:p.unit_price,unit:p.unit}))}));
  const opts = cats.map(c=>`<option value="${c.key}">${catNames[c.key]||c.key}</option>`).join('');
  const body = cats.map(c=>`
    <div class="pl-block" data-cat="${c.key}">
      <div class="pl-cat">${catNames[c.key]||c.key}<small>${c.items.length}</small></div>
      <table class="pl"><thead><tr><th>${t('pl.col.p')}</th><th>${t('pl.col.eur')}</th><th>${t('pl.col.gbp')}</th><th>${t('pl.col.unit')}</th></tr></thead>
      <tbody>${c.items.map(it=>`<tr class="plrow"><td>${it.name}</td><td><b>${eur(it.eur)}</b></td><td>${gbp(it.gbp)}</td><td style="color:var(--ink2)">${it.unit_price? eur(it.unit_price)+'/'+(it.unit==='kg'?'kg':'st.'):''}</td></tr>`).join('')}</tbody></table>
    </div>`).join('');
  return `<section><div class="wrap" style="max-width:1000px">
    <div class="sec-head"><div class="kicker">Tabac Luxe · 503</div><h2>${t('pl.title')}</h2><div class="rule"></div>
    <p style="color:var(--ink2);max-width:640px;margin:1rem auto 0">${t('pl.sub')}</p></div>
    <div class="pl-tools">
      <input id="plq" placeholder="${t('pl.search')}" oninput="plFilter()">
      <select id="plcat" onchange="plFilter()"><option value="">${t('pl.allcats')}</option>${opts}</select>
      <a class="btn dark" href="${CONFIG.pdfPath}" download>↓ ${t('pl.dl')}</a>
    </div>
    <div id="plBody">${body}</div>
    <p class="pl-note">${t('pl.note')}</p>
  </div></section>`;
}
function cat_key(en){return {'Tobacco bucket':'seau','Tobacco tin':'pot','Tobacco tin high volume':'potvol','Pipe tobacco':'pipe','Rolling tobacco':'rouler','Shisha tobacco':'shisha','Cigars':'cigares','Cigarettes':'cigarettes'}[en]||en;}
window.plFilter = function(){
  const q=(document.getElementById('plq').value||'').toLowerCase();
  const c=document.getElementById('plcat').value;
  document.querySelectorAll('.pl-block').forEach(b=>{
    const okc = !c || b.dataset.cat===c;
    let any=false;
    b.querySelectorAll('.plrow').forEach(r=>{
      const ok = !q || r.cells[0].textContent.toLowerCase().includes(q);
      r.style.display = ok?'':'none'; if(ok) any=true;
    });
    b.style.display = okc && any ? '' : 'none';
  });
};

function viewCart(){
  const entries=Object.entries(cart);
  if(!entries.length) return `<section><div class="wrap"><div class="empty">
    <h2 style="font-size:2.4rem;margin-bottom:1rem">${t('cart.title')}</h2>
    <p>${t('cart.empty')}</p><p style="margin-top:1.6rem"><a class="btn dark" href="#/catalogue">${t('cart.browse')}</a></p></div></div></section>`;
  const rows=entries.map(([sl,q])=>{
    const p=DB.products.find(x=>x.slug===sl); if(!p) return '';
    return `<div class="cartrow">
      ${p.image? `<img src="${imgOpt(p.image,120)}" width="56" height="56" alt="">`:'<span></span>'}
      <div><b class="serif" style="font-size:1.1rem">${p.name}</b><br>
      <span style="font-size:.78rem;color:var(--ink2)">${p.price_eur? eur(p.price_eur):t('card.ask')}</span></div>
      <div class="qty"><button onclick="setQty('${sl}',${q-1})">−</button><span>${q}</span><button onclick="setQty('${sl}',${q+1})">+</button></div>
      <b class="serif" style="font-size:1.2rem">${p.price_eur? eur(p.price_eur*q):'—'}</b></div>`;
  }).join('');
  return `<section><div class="wrap" style="max-width:820px">
    <div class="sec-head"><div class="kicker">Tabac Luxe</div><h2>${t('cart.title')}</h2><div class="rule"></div></div>
    ${rows}
    <div class="total-bar"><span style="letter-spacing:.2em;text-transform:uppercase;font-size:.74rem">${t('cart.total')}</span><b>${eur(cartTotal())}</b></div>
    <p style="font-size:.8rem;color:var(--ink2);margin-bottom:1.2rem">${t('cart.note')}</p>
    <button class="btn" style="width:100%" onclick="waCart()">${t('cart.order')}</button>
  </div></section>`;
}

function viewContact(){
  return `<section><div class="wrap" style="max-width:1000px">
    <div class="sec-head"><div class="kicker">Tabac Luxe</div><h2>${t('contact.title')}</h2><div class="rule"></div></div>
    <div class="split" style="border:1px solid var(--line)">
      <div class="txt" style="padding:2.6rem">
        <h3 class="serif" style="font-size:1.5rem;margin-bottom:1rem">Tabac Luxe</h3>
        <p>${CONFIG.address}</p>
        <p><a href="mailto:${CONFIG.email}" style="color:var(--gold2)">${CONFIG.email}</a><br><a href="tel:+35228777996" style="color:var(--gold2)">${CONFIG.phone}</a></p>
        <ul style="list-style:none;margin:1rem 0">
          <li style="display:flex;justify-content:space-between;border-bottom:1px solid var(--line);padding:.4rem 0"><span>${t('hours.monfri')}</span><b>06:00 – 18:00</b></li>
          <li style="display:flex;justify-content:space-between;border-bottom:1px solid var(--line);padding:.4rem 0"><span>${t('hours.sat')}</span><b>08:00 – 17:00</b></li>
          <li style="display:flex;justify-content:space-between;padding:.4rem 0"><span>${t('hours.sun')}</span><b class="closed">${t('hours.closed')}</b></li>
        </ul>
        <div class="btnrow" style="justify-content:flex-start">
          <a class="btn" target="_blank" rel="noopener" href="https://www.google.com/maps/search/?api=1&query=${encodeURIComponent(CONFIG.address)}">${t('contact.map')}</a>
          <a class="btn ghost" style="color:var(--ink);border-color:var(--ink)" href="https://wa.me/${CONFIG.whatsapp}" target="_blank" rel="noopener">WhatsApp</a>
        </div>
      </div>
      <div class="img" style="background-image:url('${imgOpt('assets/hero/boutique.jpg',900,72)}');min-height:380px"></div>
    </div>
  </div></section>`;
}
/* ================= LEGAL ================= */
const LEGAL = {
terms:{fr:`
<p class="updated">Dernière mise à jour : septembre 2026</p>
<h3>1. Objet</h3>
<p>Les présentes conditions générales régissent l'utilisation du site vitrine tabacluxe.lu, édité par Tabac Luxe S.à r.l., Route de Longwy 549, L-4832, Luxembourg (ci-après « Tabac Luxe »). Le site a une fonction exclusivement informative et de présentation.</p>
<h3>2. Absence de vente en ligne</h3>
<p>Tabac Luxe ne propose <b>aucune vente en ligne, aucun paiement en ligne et aucune livraison ou expédition</b>. Le panier et la commande via WhatsApp constituent uniquement une demande de réservation sans valeur contractuelle. Tout achat est conclu et payé exclusivement en magasin, après vérification de l'âge de l'acheteur.</p>
<h3>3. Restriction d'âge</h3>
<p>Conformément à la législation luxembourgeoise, la vente de produits du tabac et d'alcool est strictement réservée aux personnes majeures (18 ans et plus). Une pièce d'identité peut être exigée en magasin. L'accès au site est subordonné à la confirmation de votre majorité.</p>
<h3>4. Prix et disponibilités</h3>
<p>Les prix affichés sont les prix magasin en euros (TTC) et, à titre indicatif, en livres sterling. Malgré notre vigilance, des erreurs peuvent subsister : en cas de divergence, le prix affiché en magasin fait foi. Les promotions sont valables dans la limite des stocks disponibles.</p>
<h3>5. Propriété intellectuelle</h3>
<p>L'ensemble des contenus du site (textes, visuels, logo Tabac Luxe) est protégé. Les marques de produits présentées appartiennent à leurs détenteurs respectifs ; les visuels sont utilisés à des fins d'illustration des produits effectivement vendus en magasin.</p>
<h3>6. Droit applicable</h3>
<p>Les présentes conditions sont soumises au droit luxembourgeois. Tout litige relève des tribunaux du Grand-Duché de Luxembourg.</p>`,
en:`
<p class="updated">Last updated: September 2026</p>
<h3>1. Purpose</h3>
<p>These terms govern the use of the showcase website tabacluxe.lu, published by Tabac Luxe S.à r.l., Route de Longwy 549, L-4832, Luxembourg. The website is purely informational.</p>
<h3>2. No online sales</h3>
<p>Tabac Luxe offers <b>no online sales, no online payment and no delivery or shipping</b>. The cart and WhatsApp ordering are reservation requests only, without contractual value. Every purchase is concluded and paid exclusively in store, after age verification.</p>
<h3>3. Age restriction</h3>
<p>Under Luxembourg law, tobacco and alcohol may only be sold to adults (18+). ID may be required in store. Access to this site requires confirmation that you are of legal age.</p>
<h3>4. Prices and availability</h3>
<p>Displayed prices are in-store prices in euros (VAT included) and, for information, in pounds sterling. In case of discrepancy, the in-store price prevails. Promotions are valid while stocks last.</p>
<h3>5. Intellectual property</h3>
<p>All site content is protected. Product trademarks belong to their respective owners; images illustrate products actually sold in store.</p>
<h3>6. Governing law</h3>
<p>These terms are governed by the laws of the Grand Duchy of Luxembourg.</p>`},
privacy:{fr:`
<p class="updated">Dernière mise à jour : septembre 2026 — Conforme au RGPD (UE) 2016/679</p>
<h3>1. Responsable de traitement</h3>
<p>Tabac Luxe S.à r.l., Route de Longwy 549, L-4832, Luxembourg — info@tabacluxe.lu — +352 28 77 79 96.</p>
<h3>2. Données collectées</h3>
<p>Ce site ne comporte <b>aucun formulaire de compte, aucun paiement et aucun cookie de suivi publicitaire</b>. Sont uniquement utilisés :</p>
<ul>
<li><b>Stockage local de votre navigateur</b> (localStorage/sessionStorage) pour mémoriser votre langue, votre panier et votre confirmation d'âge. Ces données ne quittent jamais votre appareil.</li>
<li><b>WhatsApp</b> : si vous cliquez sur un bouton de commande, vous êtes redirigé vers WhatsApp (Meta Platforms), qui applique sa propre politique de confidentialité.</li>
<li><b>Espace administrateur</b> : l'accès est protégé et réservé au personnel autorisé.</li>
</ul>
<h3>3. Base légale et finalités</h3>
<p>Le stockage local repose sur votre consentement technique et est strictement nécessaire au fonctionnement du site. Aucune donnée personnelle n'est vendue, louée ou transmise à des tiers à des fins commerciales.</p>
<h3>4. Vos droits</h3>
<p>Conformément au RGPD, vous disposez de droits d'accès, de rectification, d'effacement, de limitation et d'opposition. Écrivez à info@tabacluxe.lu. Vous pouvez également saisir la CNPD (Commission Nationale pour la Protection des Données, Luxembourg).</p>
<h3>5. Sécurité</h3>
<p>Le catalogue et les promotions sont gérés via une infrastructure cloud sécurisée (Supabase, région UE) avec chiffrement en transit (HTTPS).</p>`,
en:`
<p class="updated">Last updated: September 2026 — GDPR (EU) 2016/679 compliant</p>
<h3>1. Data controller</h3>
<p>Tabac Luxe S.à r.l., Route de Longwy 549, L-4832, Luxembourg — info@tabacluxe.lu — +352 28 77 79 96.</p>
<h3>2. Data collected</h3>
<p>This site has <b>no account forms, no payments and no advertising trackers</b>. Only the following are used:</p>
<ul>
<li><b>Browser local storage</b> (localStorage/sessionStorage) to remember your language, cart and age confirmation. This data never leaves your device.</li>
<li><b>WhatsApp</b>: clicking an order button redirects you to WhatsApp (Meta Platforms), under its own privacy policy.</li>
<li><b>Admin area</b>: access is restricted to authorized staff.</li>
</ul>
<h3>3. Legal basis and purposes</h3>
<p>Local storage is strictly necessary for the site to function. No personal data is sold, rented or shared with third parties for commercial purposes.</p>
<h3>4. Your rights</h3>
<p>Under GDPR you have the rights of access, rectification, erasure, restriction and objection. Write to info@tabacluxe.lu. You may also contact the CNPD (Luxembourg).</p>
<h3>5. Security</h3>
<p>The catalogue and promotions are managed on secure cloud infrastructure (Supabase, EU region) with encryption in transit (HTTPS).</p>`},
disclaimer:{fr:`
<p class="updated">Dernière mise à jour : septembre 2026</p>
<h3>Avertissement sanitaire</h3>
<p><b>Fumer tue. Le tabac crée une forte dépendance.</b> L'abus d'alcool est dangereux pour la santé, à consommer avec modération. La vente de tabac et d'alcool est interdite aux mineurs de moins de 18 ans. Pour arrêter de fumer : Tabac Stop Line 8002 6767 — www.tabac-stop.lu.</p>
<h3>Nature du site</h3>
<p>Ce site est une <b>vitrine informative</b>. Il ne constitue ni une offre de vente à distance, ni une incitation à consommer du tabac ou de l'alcool. Les informations (prix, disponibilités, visuels) sont données à titre indicatif et peuvent évoluer sans préavis ; le prix en magasin fait foi.</p>
<h3>Visuels des produits</h3>
<p>Les photographies illustrent les produits effectivement commercialisés. Les emballages vendus au Luxembourg comportent les avertissements sanitaires réglementaires. Les marques citées appartiennent à leurs propriétaires respectifs.</p>
<h3>Responsabilité</h3>
<p>Tabac Luxe décline toute responsabilité en cas d'utilisation du site par un mineur ayant confirmé mensongèrement sa majorité, ainsi qu'en cas d'interruption ou d'erreur technique temporaire.</p>`,
en:`
<p class="updated">Last updated: September 2026</p>
<h3>Health warning</h3>
<p><b>Smoking kills. Tobacco is highly addictive.</b> Alcohol abuse is dangerous for your health — consume in moderation. The sale of tobacco and alcohol to minors under 18 is prohibited. Quit smoking: Tabac Stop Line 8002 6767 — www.tabac-stop.lu.</p>
<h3>Nature of this site</h3>
<p>This website is an <b>informational showcase</b>. It is neither a distance-selling offer nor an incentive to consume tobacco or alcohol. Information (prices, availability, images) is indicative and may change without notice; the in-store price prevails.</p>
<h3>Product images</h3>
<p>Photographs illustrate products actually sold. Packaging sold in Luxembourg carries the mandatory health warnings. Quoted trademarks belong to their respective owners.</p>
<h3>Liability</h3>
<p>Tabac Luxe declines all liability where a minor falsely confirms legal age, and for temporary technical interruptions or errors.</p>`},
notice:{fr:`
<p class="updated">Dernière mise à jour : septembre 2026</p>
<h3>Éditeur</h3>
<p><b>Tabac Luxe S.à r.l.</b><br>Route de Longwy 549<br>L-4832<br>Grand-Duché de Luxembourg<br>E-mail : info@tabacluxe.lu<br>Tél. : +352 28 77 79 96</p>
<h3>Activité</h3>
<p>Commerce de détail de tabacs, cigares, articles pour fumeurs, boissons et produits assimilés. Établissement soumis à la législation luxembourgeoise sur la vente de tabac et d'alcool (licences en vigueur).</p>
<h3>Hébergement</h3>
<p>Site statique hébergé sur infrastructure cloud ; base de données catalogue : Supabase (région UE, eu-west-1).</p>
<h3>Directeur de la publication</h3>
<p>La direction de Tabac Luxe S.à r.l.</p>`,
en:`
<p class="updated">Last updated: September 2026</p>
<h3>Publisher</h3>
<p><b>Tabac Luxe S.à r.l.</b><br>Route de Longwy 549<br>L-4832<br>Grand Duchy of Luxembourg<br>Email: info@tabacluxe.lu<br>Tel: +352 28 77 79 96</p>
<h3>Activity</h3>
<p>Retail of tobacco, cigars, smokers' articles, beverages and related products, operated under Luxembourg law on tobacco and alcohol sales (current licences).</p>
<h3>Hosting</h3>
<p>Static site hosted on cloud infrastructure; catalogue database: Supabase (EU region, eu-west-1).</p>
<h3>Publication director</h3>
<p>The management of Tabac Luxe S.à r.l.</p>`}
};
function viewLegal(key){
  const l=LEGAL[key]; if(!l) return viewHome();
  const body=l[LANG]||l.fr||l.en;
  return `<section><div class="wrap legal">
    <h2>${t('legal.title.'+key)}</h2>
    ${body}
    <p style="margin-top:2.4rem"><a class="btn ghost" style="color:var(--ink);border-color:var(--ink)" href="#/">← ${t('nav.home')}</a></p>
  </div></section>`;
}

/* ================= ADMIN ================= */
let adminTab='products';
function isAdmin(){ return sessionStorage.getItem('tl_admin')==='1'; }
function adminLogin(){
  const v=document.getElementById('apass').value;
  if(v===CONFIG.adminPass){ sessionStorage.setItem('tl_admin','1'); render(); }
  else toast('—');
}
async function saveProduct(id){
  const row=document.querySelector(`tr[data-id="${id}"]`);
  const patch={
    name: row.querySelector('.f-name').value,
    price_eur: row.querySelector('.f-eur').value===''?null:parseFloat(row.querySelector('.f-eur').value.replace(',','.')),
    price_gbp: row.querySelector('.f-gbp').value===''?null:parseFloat(row.querySelector('.f-gbp').value.replace(',','.')),
    featured: row.querySelector('.f-feat').checked,
    deal: row.querySelector('.f-deal').checked,
    active: row.querySelector('.f-act').checked,
    updated_at: new Date().toISOString()
  };
  try{
    await api(`products?id=eq.${id}`,{method:'PATCH',body:JSON.stringify(patch)});
    const p=DB.products.find(x=>x.id===id); Object.assign(p,patch);
    toast(t('admin.saved'));
  }catch(e){ toast('Error'); }
}
async function delPromo(id){
  try{ await api(`promos?id=eq.${id}`,{method:'DELETE'}); DB.promos=DB.promos.filter(p=>p.id!==id); render(); }catch(e){toast('Error');}
}
async function savePromo(id){
  const row=document.querySelector(`tr[data-pid="${id}"]`);
  const patch={ title:{...((DB.promos.find(p=>p.id===id)||{}).title||{}),fr:row.querySelector('.p-title').value},
    body:{...((DB.promos.find(p=>p.id===id)||{}).body||{}),fr:row.querySelector('.p-body').value},
    badge:row.querySelector('.p-badge').value, active:row.querySelector('.p-act').checked };
  try{
    await api(`promos?id=eq.${id}`,{method:'PATCH',body:JSON.stringify(patch)});
    Object.assign(DB.promos.find(p=>p.id===id),patch); toast(t('admin.saved'));
  }catch(e){toast('Error');}
}
async function addPromo(){
  try{
    const r=await api('promos',{method:'POST',headers:{Prefer:'return=representation'},body:JSON.stringify({title:{fr:'Nouvelle promotion'},body:{fr:''},badge:'Promo',active:true,sort:99})});
    DB.promos.push(r[0]); render();
  }catch(e){toast('Error');}
}
function viewAdmin(){
  if(!isAdmin()) return `<section><div class="wrap"><div class="loginbox">
    <h2 class="serif" style="font-size:1.7rem">${t('admin.login')}</h2>
    <input id="apass" type="password" placeholder="${t('admin.pass')}" onkeydown="if(event.key==='Enter')adminLogin()">
    <button class="btn dark" style="width:100%" onclick="adminLogin()">${t('admin.enter')}</button>
  </div></div></section>`;
  let body='';
  if(adminTab==='products'){
    body=`<input id="aq" placeholder="${t('admin.search')}" oninput="adminFilter()" style="padding:.7rem 1rem;border:1px solid var(--line);width:100%;max-width:340px;margin-bottom:1rem">
    <div style="overflow-x:auto"><table class="atable" id="atable"><thead><tr>
      <th>ID</th><th>Nom</th><th>Cat.</th><th>€</th><th>£</th><th>Vedette</th><th>Promo</th><th>Actif</th><th></th></tr></thead><tbody>
      ${DB.products.map(p=>`<tr data-id="${p.id}" class="arow">
        <td>${p.id}</td><td><input class="f-name" value="${p.name.replace(/"/g,'&quot;')}"></td>
        <td><span class="tag">${p.category}</span></td>
        <td style="width:90px"><input class="f-eur" value="${p.price_eur??''}"></td>
        <td style="width:90px"><input class="f-gbp" value="${p.price_gbp??''}"></td>
        <td><input type="checkbox" class="f-feat" ${p.featured?'checked':''}></td>
        <td><input type="checkbox" class="f-deal" ${p.deal?'checked':''}></td>
        <td><input type="checkbox" class="f-act" ${p.active!==false?'checked':''}></td>
        <td><button class="mini gold" onclick="saveProduct(${p.id})">${t('admin.save')}</button></td></tr>`).join('')}
    </tbody></table></div>`;
  }else{
    body=`<button class="mini gold" style="margin-bottom:1rem;padding:.6rem 1.2rem" onclick="addPromo()">+ ${t('admin.addpromo')}</button>
    <table class="atable"><thead><tr><th>Badge</th><th>Titre (FR)</th><th>Texte (FR)</th><th>Active</th><th></th></tr></thead><tbody>
    ${DB.promos.map(pr=>`<tr data-pid="${pr.id}">
      <td style="width:110px"><input class="p-badge" value="${(pr.badge||'').replace(/"/g,'&quot;')}"></td>
      <td><input class="p-title" value="${((pr.title&&pr.title.fr)||'').replace(/"/g,'&quot;')}"></td>
      <td><input class="p-body" value="${((pr.body&&pr.body.fr)||'').replace(/"/g,'&quot;')}"></td>
      <td><input type="checkbox" class="p-act" ${pr.active?'checked':''}></td>
      <td><button class="mini gold" onclick="savePromo(${pr.id})">${t('admin.save')}</button>
      <button class="mini red" onclick="delPromo(${pr.id})">${t('admin.del')}</button></td></tr>`).join('')}
    </tbody></table>`;
  }
  return `<div class="admin-bar"><span>Tabac Luxe · Admin</span><span>${t('admin.hint')} <button onclick="sessionStorage.removeItem('tl_admin');render()">${t('admin.logout')}</button></span></div>
  <section style="padding:2rem 0"><div class="wrap" style="max-width:1240px">
    <div style="display:flex;gap:.6rem;margin-bottom:1.2rem">
      <button class="mini ${adminTab==='products'?'gold':''}" onclick="adminTab='products';render()">${t('admin.products')} (${DB.products.length})</button>
      <button class="mini ${adminTab==='promos'?'gold':''}" onclick="adminTab='promos';render()">${t('admin.promos')} (${DB.promos.length})</button>
    </div>${body}
  </div></section>`;
}
window.adminFilter=function(){
  const q=(document.getElementById('aq').value||'').toLowerCase();
  document.querySelectorAll('.arow').forEach(r=>{
    r.style.display = r.querySelector('.f-name').value.toLowerCase().includes(q)?'':'none';
  });
};

/* ================= ROUTER / INIT ================= */
function applyI18n(){
  document.documentElement.lang=LANG;
  document.querySelectorAll('[data-i18n]').forEach(el=>{ el.textContent=t(el.dataset.i18n); });
  document.getElementById('announceText').textContent =
    `${t('hours.monfri')} 06:00–18:00 · ${t('hours.sat')} 08:00–17:00 · ${t('hours.sun')} ${t('hours.closed')} · ${CONFIG.address} · ${CONFIG.email} · ` + t('footer.age');
  document.getElementById('wafab').href=`https://wa.me/${CONFIG.whatsapp}?text=${encodeURIComponent(t('wa.hello'))}`;
}
function buildLangs(){
  const wrap=document.getElementById('langs');
  wrap.innerHTML=['fr','de','en','pt','lb'].map(l=>`<button class="${l===LANG?'on':''}" onclick="setLang('${l}')">${l}</button>`).join('');
}
window.setLang=function(l){ LANG=l; localStorage.setItem('tl_lang',l); buildLangs(); applyI18n(); render(); };

function ageGate(){
  if(sessionStorage.getItem('tl_adult')==='1') return;
  const bg=document.createElement('div'); bg.className='modal-bg'; bg.id='ageGate';
  bg.innerHTML=`<div class="modal" role="dialog" aria-modal="true" aria-labelledby="ageTitle">
    <div class="agebadge">18+</div>
    <h2 id="ageTitle">${t('age.title')}</h2><p>${t('age.txt')}</p>
    <div class="btnrow"><button class="btn" id="ageYes">${t('age.yes')}</button>
    <button class="btn ghost" style="color:var(--ink);border-color:var(--line)" id="ageNo">${t('age.no')}</button></div>
  </div>`;
  document.body.appendChild(bg);
  document.getElementById('ageYes').onclick=()=>{sessionStorage.setItem('tl_adult','1');bg.remove();};
  document.getElementById('ageNo').onclick=()=>{bg.querySelector('.modal').innerHTML=`<h2>${t('age.sorry')}</h2>`;};
}

function route(){
  const h=(location.hash||'#/').slice(1);
  const parts=h.split('/').filter(Boolean);
  document.querySelectorAll('nav.mainnav a').forEach(a=>a.classList.toggle('on',
    a.dataset.nav===parts[0] || (!parts[0]&&a.dataset.nav==='home')));
  document.getElementById('mainnav').classList.remove('open');
  if(!parts[0]) return viewHome();
  if(parts[0]==='catalogue') return viewCatalogue(parts[1]);
  if(parts[0]==='promos') return viewPromos();
  if(parts[0]==='tarifs') return viewPriceList();
  if(parts[0]==='cart') return viewCart();
  if(parts[0]==='contact') return viewContact();
  if(parts[0]==='legal') return viewLegal(parts[1]);
  if(parts[0]==='admin') return viewAdmin();
  return viewHome();
}
async function render(){
  const app=document.getElementById('app');
  app.innerHTML=route();
  window.scrollTo({top:0});
  revealInit();
  if((location.hash||'').startsWith('#/catalogue')) catFilter();
}
async function navigate(){
  const hash = location.hash || '#/';
  if(hash !== '#/'){
    await loadData();
  }
  render();
}
window.addEventListener('hashchange',navigate);

(async function init(){
  document.body.classList.add('app-ready');
  buildLangs(); applyI18n(); updateCartN();
  setTimeout(ageGate, 8000);
  const isHome = (location.hash||'#/') === '#/';
  if(isHome){
    revealInit();
    setTimeout(async ()=>{
      await loadData();
      window.__homeBelowLoaded = true;
      const el = document.getElementById('homeDeferred');
      if(el){ el.innerHTML = homeBelowHtml(); revealInit(); }
    }, 7000);
    return;
  }
  await loadData();
  render();
})();
