# Analisi del Churn dei Clienti Telco

**Machine Learning supervisionato e non supervisionato**

## 1. Obiettivo del progetto

Questo progetto analizza il dataset **Telco Customer Churn (IBM Sample Data)** con l’obiettivo di:

* prevedere l’abbandono dei clienti (*churn*) tramite **machine learning supervisionato**
* segmentare i clienti in gruppi omogenei tramite **machine learning non supervisionato**
* applicare un processo corretto di pulizia dei dati, evitando **data leakage** e garantendo rigore metodologico

Il progetto segue un flusso **end-to-end**, dall’analisi esplorativa fino alla modellazione e interpretazione dei risultati.

---

## 2. Descrizione del dataset

* **Fonte**: Kaggle – Telco Customer Churn (IBM Sample Data)
* **Unità di analisi**: singolo cliente
* **Variabile target (supervisionato)**:

  * `Churn Label`

    * 1 = cliente che ha abbandonato
    * 0 = cliente che è rimasto
* **Variabili esplicative**:

  * caratteristiche demografiche (genere, senior citizen)
  * tipologia di contratto e metodo di pagamento
  * servizi sottoscritti (internet, streaming, supporto tecnico)
  * utilizzo e fatturazione (tenure, costi mensili, costi totali)

---

## 3. Analisi esplorativa dei dati (EDA)

La fase di EDA ha incluso:

* ispezione della struttura del dataset e dei tipi di variabili
* analisi della distribuzione del churn e dello sbilanciamento delle classi
* identificazione di valori mancanti e incoerenze
* analisi delle relazioni tra churn e variabili chiave
* matrice di correlazione per le variabili numeriche

**Principali evidenze**:

* il churn è concentrato nei primi mesi di relazione con il cliente
* i contratti *month-to-month* presentano tassi di churn più elevati
* costi mensili più alti sono associati a maggiore probabilità di churn

---

## 4. Pulizia e preparazione dei dati

### 4.1 Rimozione del data leakage

Sono state rimosse tutte le variabili contenenti informazione **ex-post** o derivate direttamente dal churn, tra cui:

* identificativi del cliente
* `Churn Reason`
* `Churn Score`
* `Churn Value`
* `CLTV`

La variabile `Churn Label` è stata mantenuta **esclusivamente** come target nel modello supervisionato.

---

### 4.2 Controlli di qualità dei dati

* conversione di variabili numeriche memorizzate come stringhe (es. costi totali)
* rimozione delle osservazioni strutturalmente incoerenti (tenure = 0)
* verifica e rimozione di eventuali duplicati
* controllo dei valori mancanti

Al termine di questa fase, il dataset risulta:

* coerente
* privo di leakage
* adatto alla modellazione

---

## 5. Machine learning supervisionato – Predizione del churn

### 5.1 Scelta del modello

È stato utilizzato **XGBoost (XGBClassifier)** in quanto:

* gestisce efficacemente non linearità e interazioni tra variabili
* è robusto agli outlier
* non richiede scaling delle feature
* gestisce valori mancanti
* garantisce ottime performance con tuning limitato

Le variabili categoriche sono state trasformate tramite **one-hot encoding**.

---

### 5.2 Addestramento e valutazione

Il processo ha incluso:

1. one-hot encoding delle variabili categoriche
2. suddivisione train/test con stratificazione
3. addestramento del modello XGBoost
4. valutazione tramite:

   * ROC-AUC
   * classification report
   * curva ROC
   * feature importance

**Risultati tipici**:

* ROC-AUC compreso tra 0.85 e 0.88
* elevata capacità discriminante tra clienti che abbandonano e clienti fedeli

Le variabili più rilevanti risultano tenure, tipologia di contratto e costi mensili.

---

## 6. Machine learning non supervisionato – Segmentazione clienti

### 6.1 Obiettivo

Identificare profili di clienti omogenei **senza utilizzare la variabile di churn**, per individuare pattern latenti nel comportamento e nelle caratteristiche dei clienti.

---

### 6.2 Metodologia

* rimozione completa di `Churn Label` dal dataset
* trattamento separato di variabili numeriche e categoriche:

  * imputazione mediana e standardizzazione per le numeriche
  * imputazione della moda e one-hot encoding per le categoriche
* applicazione di **KMeans clustering**
* visualizzazione tramite **PCA** a due dimensioni

---

### 6.3 Elbow Method

È stato applicato l’**Elbow Method** per valutare il numero appropriato di cluster, analizzando la riduzione dell’inertia al crescere di K (da 1 a 10).

Questo approccio ha permesso di:

* identificare un punto di flesso (“gomito”)
* giustificare in modo data-driven la scelta del numero di cluster
* bilanciare semplicità interpretativa e qualità della segmentazione

---

### 6.4 Interpretazione dei cluster

I cluster sono stati analizzati attraverso:

* valori medi delle variabili numeriche
* categoria più frequente per ciascuna variabile categorica
* dimensione dei cluster

Successivamente, a fini interpretativi, è possibile analizzare **ex-post** la distribuzione del churn nei cluster, senza compromettere la natura non supervisionata dell’analisi.

---



Dimmi come lo vuoi rifinire.
