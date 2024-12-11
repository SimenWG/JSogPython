// Oppgave 1 Kalkulator 

// function kalkulator() {
//     console.log("Velg operasjon:");
//     console.log("1. Addisjon");
//     console.log("2. Subtraksjon");
//     console.log("3. Multiplikasjon");
//     console.log("4. Divisjon");

//     const valg = prompt("Tast inn valg (1/2/3/4): ");
//     const tall1 = parseFloat(prompt("Tast inn første tall: "));
//     const tall2 = parseFloat(prompt("Tast inn andre tall: "));

//     switch (valg) {
//         case '1':
//             console.log(`Resultat: ${tall1} + ${tall2} = ${tall1 + tall2}`);
//             break;
//         case '2':
//             console.log(`Resultat: ${tall1} - ${tall2} = ${tall1 - tall2}`);
//             break;
//         case '3':
//             console.log(`Resultat: ${tall1} * ${tall2} = ${tall1 * tall2}`);
//             break;
//         case '4':
//             if (tall2 !== 0) {
//                 console.log(`Resultat: ${tall1} / ${tall2} = ${tall1 / tall2}`);
//             } else {
//                 console.log("Feil: Kan ikke dele med null.");
//             }
//             break;
//         default:
//             console.log("Ugyldig valg.");
//     }
// }
// kalkulator();



// Oppgave 2 Geometri

// const lengde = 6;
// const bredde = 8;
// const areal = lengde * bredde;
// console.log(`Arealet av rektangelet er ${areal} kvadratmeter.`);

// Oppgave 3 Interaktiv

// const navn = prompt("Hva heter du? ");
// const alder = parseInt(prompt("Hvor gammel er du? "), 10);
// const årTil100 = 100 - alder;
// console.log(`Hei ${navn}, du fyller 100 år om ${årTil100} år.`);

// Oppgave 4 Positiv/Negativ kontroll

// const nummer = parseFloat(prompt("Tast inn et tall: "));

// if (nummer > 0) {
//     console.log("Tallet er positivt.");
// } else if (nummer < 0) {
//     console.log("Tallet er negativt.");
// } else {
//     console.log("Tallet er null.");
// }

// Oppgave 5 SUM

// const n = parseInt(prompt("Tast inn et tall: "), 10);
// let sumTall = 0;
// for (let i = 1; i <= n; i++) {
//     sumTall += i;
// }
// console.log(`Summen av tallene fra 1 til ${n} er ${sumTall}.`);

// Oppgave 6 Listebehandling

// const navnListe = [];
// navnListe.push(prompt("Tast inn navn 1: "));
// navnListe.push(prompt("Tast inn navn 2: "));
// navnListe.push(prompt("Tast inn navn 3: "));
// navnListe.push(prompt("Tast inn navn 4: "));
// navnListe.push(prompt("Tast inn navn 5: "));
// console.log(`Navnelisten: ${navnListe}`);

// Oppgave 7 Listebehandling 2

// const navnListe = [];
// for (let i = 0; i < 5; i++) {
//     const navn = prompt(`Tast inn navn ${i + 1}: `);
//     navnListe.push(navn);
// }
// console.log(`Navnelisten: ${navnListe}`);

// Oppgave 8 Funksjonsbruk

// function sorterOgBeregneGjennomsnitt(liste) {
//     liste.sort((a, b) => a - b);
//     const gjennomsnitt = liste.reduce((a, b) => a + b, 0) / liste.length;
//     return gjennomsnitt;
// }

// const resultat = sorterOgBeregneGjennomsnitt([4, 1, 7, 3, 9]);
// console.log(`Gjennomsnittet er ${resultat}`);

// Oppgave 9 Snurr

// const liste = [1, 2, 3, 4, 5];
// const snuddListe = liste.slice().reverse();
// console.log(`Den snudde listen: ${snuddListe}`);