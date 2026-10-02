import streamlit as st
import requests
from streamlit_lottie import st_lottie

# ---------------------------------------------------------
# CONFIGURACIÓN
# ---------------------------------------------------------
st.set_page_config(
    page_title="SIMG · Semillero HPC & IA Generativa",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ---------------------------------------------------------
# LOTTIE
# ---------------------------------------------------------
@st.cache_data(show_spinner=False)
def load_lottieurl(url: str):
    try:
        r = requests.get(url, timeout=5)
        if r.status_code != 200:
            return None
        return r.json()
    except Exception:
        return None

lottie_ai     = load_lottieurl("https://lottie.host/78625b82-bc12-4217-a066-6fc3c77e6fcd/4k8Z1l0A2c.json")
lottie_cpu    = load_lottieurl("https://lottie.host/4a5b4c1a-28a5-48fa-acb6-ec6c58de8cf7/4fTqFq9p9G.json")
lottie_rocket = load_lottieurl("https://lottie.host/9082eb4c-ad2e-4613-8a3c-b2ddfb1df555/kSj9s7D6l9.json")

# ---------------------------------------------------------
# CSS GLOBAL
# ---------------------------------------------------------
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;800;900&family=JetBrains+Mono:wght@400;600&display=swap');

html, body, [class*="css"] { font-family: 'Inter', sans-serif; }

.stApp {
    background:
      radial-gradient(ellipse at 10% 0%, rgba(34,211,238,0.10) 0%, transparent 45%),
      radial-gradient(ellipse at 90% 10%, rgba(192,132,252,0.10) 0%, transparent 45%),
      radial-gradient(circle at 50% 100%, #0f172a 0%, #020617 60%, #000 100%);
    color: #e2e8f0;
}

section[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #0b1220 0%, #020617 100%);
    border-right: 1px solid rgba(34,211,238,0.15);
}
section[data-testid="stSidebar"] * { color: #cbd5e1 !important; }

.neon-title {
    background: linear-gradient(90deg, #22d3ee 0%, #818cf8 50%, #c084fc 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    font-weight: 900;
    font-size: 3rem;
    letter-spacing: -0.03em;
    line-height: 1.05;
    margin-bottom: 4px;
}
.neon-title.sm { font-size: 2.2rem; }

.subtitle {
    color: #94a3b8;
    font-size: 1.1rem;
    font-weight: 400;
    margin-top: 0;
    line-height: 1.5;
}

@keyframes fadeUp {
    from { opacity: 0; transform: translateY(18px); }
    to   { opacity: 1; transform: translateY(0); }
}
.fade-in { animation: fadeUp 0.7s ease both; }

/* KPI */
.kpi {
    background: linear-gradient(145deg, rgba(30,41,59,0.7), rgba(15,23,42,0.7));
    border: 1px solid rgba(99,102,241,0.25);
    border-radius: 16px;
    padding: 20px 22px;
    animation: fadeUp 0.6s ease both;
    backdrop-filter: blur(6px);
    transition: transform 0.25s, border-color 0.25s;
}
.kpi:hover { transform: translateY(-4px); border-color: rgba(34,211,238,0.5); }
.kpi-label { color: #94a3b8; font-size: 0.78rem; text-transform: uppercase; letter-spacing: 0.12em; }
.kpi-value { color: #f1f5f9; font-size: 2.1rem; font-weight: 800; letter-spacing: -0.02em; margin-top: 4px; }

/* Pilar cards */
.pillar {
    background: linear-gradient(150deg, rgba(30,41,59,0.55), rgba(15,23,42,0.55));
    border: 1px solid rgba(148,163,184,0.15);
    border-radius: 18px;
    padding: 24px 22px 20px 22px;
    height: 100%;
    position: relative;
    overflow: hidden;
    transition: transform 0.3s, border-color 0.3s, box-shadow 0.3s;
    animation: fadeUp 0.7s ease both;
}
.pillar:hover {
    transform: translateY(-6px);
    border-color: rgba(34,211,238,0.45);
    box-shadow: 0 18px 40px -18px rgba(34,211,238,0.4);
}
.pillar::before {
    content: "";
    position: absolute; top: 0; left: 0; right: 0; height: 3px;
    background: linear-gradient(90deg, #22d3ee, #818cf8, #c084fc);
}
.pillar-icon { font-size: 2.2rem; margin-bottom: 8px; }
.pillar-title {
    color: #f1f5f9; font-weight: 700; font-size: 1.15rem; margin-bottom: 8px;
    letter-spacing: -0.01em;
}
.pillar-text { color: #cbd5e1; font-size: 0.94rem; line-height: 1.55; }

/* Badge */
.badge {
    display: inline-block;
    padding: 4px 12px;
    border-radius: 999px;
    font-size: 0.72rem;
    font-weight: 600;
    margin-right: 6px;
    background: rgba(34,211,238,0.15);
    color: #22d3ee;
    border: 1px solid rgba(34,211,238,0.35);
    letter-spacing: 0.03em;
}
.badge-purple { background: rgba(192,132,252,0.15); color: #c084fc; border-color: rgba(192,132,252,0.35); }
.badge-amber  { background: rgba(251,191,36,0.15); color: #fbbf24; border-color: rgba(251,191,36,0.35); }
.badge-rose   { background: rgba(244,114,182,0.15); color: #f472b6; border-color: rgba(244,114,182,0.35); }

/* Timeline sesión (barra horizontal) */
.session-tl {
    display: flex;
    width: 100%;
    height: 110px;
    border-radius: 16px;
    overflow: hidden;
    border: 1px solid rgba(148,163,184,0.18);
    margin: 6px 0 8px 0;
    box-shadow: 0 12px 30px -18px rgba(0,0,0,0.8);
}
.tl-seg {
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    color: white;
    padding: 10px;
    text-align: center;
    position: relative;
    transition: filter 0.2s;
}
.tl-seg:hover { filter: brightness(1.15); }
.tl-seg .lbl { font-weight: 700; font-size: 1rem; letter-spacing: -0.01em; }
.tl-seg .min { font-size: 0.8rem; opacity: 0.85; margin-top: 4px; font-family: 'JetBrains Mono', monospace; }
.tl-seg.cyan  { background: linear-gradient(135deg, #0891b2, #22d3ee); }
.tl-seg.indigo{ background: linear-gradient(135deg, #4f46e5, #818cf8); }
.tl-seg.pink  { background: linear-gradient(135deg, #db2777, #f472b6); }
.tl-total {
    display: flex; justify-content: space-between; align-items: center;
    color: #94a3b8; font-size: 0.85rem; padding: 0 4px;
}
.tl-total strong { color: #e2e8f0; font-family: 'JetBrains Mono', monospace; }

/* Roadmap item */
.tl-item {
    border-left: 2px solid rgba(99,102,241,0.4);
    padding: 12px 0 12px 22px;
    position: relative;
    animation: fadeUp 0.5s ease both;
}
.tl-item::before {
    content: "";
    position: absolute;
    left: -8px; top: 20px;
    width: 14px; height: 14px;
    background: linear-gradient(135deg, #22d3ee, #818cf8);
    border-radius: 50%;
    box-shadow: 0 0 14px rgba(34,211,238,0.75);
}
.tl-num  { color: #22d3ee; font-family: 'JetBrains Mono', monospace; font-size: 0.78rem; letter-spacing: 0.1em; }
.tl-title{ color: #f1f5f9; font-weight: 700; font-size: 1.08rem; margin: 2px 0; }
.tl-sub  { color: #94a3b8; font-size: 0.9rem; }

/* Bloque de contenido dentro de expander */
.info-block {
    padding: 14px 18px;
    border-radius: 12px;
    margin-bottom: 12px;
    font-size: 0.96rem;
    line-height: 1.6;
}
.info-tema { background: rgba(34,211,238,0.08); border-left: 3px solid #22d3ee; color: #cffafe; }
.info-obj  { background: rgba(34,197,94,0.08); border-left: 3px solid #22c55e; color: #dcfce7; }
.info-prac { background: rgba(251,191,36,0.08); border-left: 3px solid #fbbf24; color: #fef3c7; }
.info-lec  { background: rgba(192,132,252,0.08); border-left: 3px solid #c084fc; color: #ede9fe; font-style: italic; }
.info-label {
    font-size: 0.78rem; font-weight: 700; letter-spacing: 0.08em;
    text-transform: uppercase; opacity: 0.85; margin-bottom: 4px;
}

code { font-family: 'JetBrains Mono', monospace; color: #67e8f9 !important; }

div[role="radiogroup"] label {
    padding: 8px 12px !important;
    border-radius: 10px !important;
    transition: background 0.2s;
}
div[role="radiogroup"] label:hover {
    background: rgba(34,211,238,0.08) !important;
}

hr { border-color: rgba(148,163,184,0.12) !important; }

details {
    background: rgba(15,23,42,0.55) !important;
    border: 1px solid rgba(148,163,184,0.15) !important;
    border-radius: 14px !important;
    margin-bottom: 10px !important;
    transition: border-color 0.25s !important;
}
details:hover { border-color: rgba(34,211,238,0.35) !important; }
details summary {
    font-weight: 600 !important;
    color: #e2e8f0 !important;
    padding: 12px 16px !important;
}
</style>
""", unsafe_allow_html=True)

# ---------------------------------------------------------
# DATA: SESIONES
# ---------------------------------------------------------
sesiones = [
    {"n":1,  "icon":"🔥","title":"El Motor de la IA","sub":"¿Por qué GenAI necesita HPC?",
     "tag":"Fundamentos","badge":"badge",
     "tema":"Contexto de HPC. Modelos de Difusión, VAEs, Flow Matching y LLMs. Límite por cómputo vs memoria. Roofline Model.",
     "obj":"Entender dónde está el cuello de botella matemático de un modelo antes de optimizarlo.",
     "prac":"Calcular puntos en el Roofline para un bloque Transformer vs. una convolución.",
     "lec":"Williams et al. (2009) — Roofline Model"},
    {"n":2,  "icon":"🧬","title":"Anatomía de un Monstruo","sub":"Hardware y Memoria",
     "tag":"Hardware","badge":"badge-purple",
     "tema":"CPU vs GPU. NVLink vs PCIe. Jerarquía: Registros, L1/L2, Shared Memory, HBM (VRAM).",
     "obj":"Comprender físicamente cómo viajan los datos y por qué moverlos cuesta más que multiplicarlos.",
     "prac":"Dibujar un diagrama de flujo de datos (I/O) de un forward pass simple. <i>(+ Socialización de nuevos miembros)</i>",
     "lec":"NVIDIA CUDA Programming Guide — Memory Hierarchy"},
    {"n":3,  "icon":"⚖️","title":"El Arte de lo Suficiente","sub":"Mixed Precision",
     "tag":"Precisión","badge":"badge-amber",
     "tema":"Formatos FP64 → FP8, INT8. Acumulación. Loss scaling y estabilidad numérica.",
     "obj":"Entrenar más rápido y usar menos memoria sin colapsar las matemáticas del modelo.",
     "prac":"Entrenar un VAE pequeño midiendo VRAM y loss en FP32 vs BF16 vs FP16 con AMP.",
     "lec":"Micikevicius et al. (2018) — Mixed Precision Training"},
    {"n":4,  "icon":"💬","title":"Hablando con el Silicio","sub":"CUDA y Triton",
     "tag":"Kernels","badge":"badge",
     "tema":"Modelo de ejecución de GPUs (Grid, Blocks, Warps/Threads). Introducción a Triton (OpenAI).",
     "obj":"Perder el miedo al bajo nivel y entender el paralelismo masivo real de las GPUs.",
     "prac":"Implementar suma de vectores y activación (SiLU) en Triton vs PyTorch puro.",
     "lec":"Tutorial oficial de Triton (OpenAI) — Partes 1 y 2"},
    {"n":5,  "icon":"⚡","title":"Exprimiendo la Memoria","sub":"Tiling y FlashAttention",
     "tag":"Kernels","badge":"badge",
     "tema":"Multiplicación de matrices. Memory coalescing, Tiling. FlashAttention (I/O awareness, online softmax).",
     "obj":"Comprender el algoritmo que revolucionó el tamaño de contexto en LLMs y Difusión.",
     "prac":"Implementar un Matmul con tiling en Triton.",
     "lec":"Dao et al. (2022) — FlashAttention · Dao (2023) — FlashAttention-2"},
    {"n":6,  "icon":"🌐","title":"Comunicaciones en el Clúster","sub":"MPI y Redes",
     "tag":"Distribuido","badge":"badge-purple",
     "tema":"Infiniband, switches. Paradigmas MPI. Colectivas: All-reduce, All-gather. Ring vs Tree.",
     "obj":"Entender cómo sincronizar gradientes o pesos evitando cuellos de botella de red.",
     "prac":"Trazar y perfilar tiempos de comunicación vs cómputo usando <code>torch.distributed</code>.",
     "lec":"NVIDIA NCCL Docs · Tutorial de PyTorch Distributed"},
    {"n":7,  "icon":"🏗️","title":"Entrenando Gigantes","sub":"Paralelismo SOTA",
     "tag":"Distribuido","badge":"badge-purple",
     "tema":"Data Parallel, Tensor Parallel (Megatron), Pipeline Parallel, ZeRO / FSDP.",
     "obj":"Saber qué técnica de paralelismo elegir según el tamaño del modelo y el clúster.",
     "prac":"Ejecutar un entrenamiento con FSDP en múltiples GPUs simuladas/reales.",
     "lec":"Shoeybi et al. (2019) — Megatron-LM · Rajbhandari et al. (2020) — ZeRO"},
    {"n":8,  "icon":"🎯","title":"Hackeando la Escala","sub":"PEFT y Adaptadores",
     "tag":"Eficiencia","badge":"badge-amber",
     "tema":"LoRA, QLoRA, DoRA. Hipótesis del rango intrínseco. Impacto en memoria de gradientes/optimizador.",
     "obj":"Democratizar el entrenamiento: adaptar modelos masivos con bajo presupuesto de VRAM.",
     "prac":"Fine-tuning (LoRA) de un LLM o difusión en una sola GPU reportando ahorro.",
     "lec":"Hu et al. (2021) — LoRA · Dettmers et al. (2023) — QLoRA"},
    {"n":9,  "icon":"📦","title":"Aligerando el Peso","sub":"Cuantización",
     "tag":"Eficiencia","badge":"badge-amber",
     "tema":"PTQ vs QAT. Weight-only. GPTQ, AWQ. Precisión vs degradación.",
     "obj":"Reducir modelos para despliegue entendiendo la matemática de la pérdida de información.",
     "prac":"Cuantizar un modelo (~1B) a 4-bit y medir honestamente la degradación.",
     "lec":"Frantar et al. (2022) — GPTQ · Lin et al. (2023) — AWQ"},
    {"n":10, "icon":"🔬","title":"La Verdad en los Datos","sub":"Inferencia y Profiling",
     "tag":"Cierre","badge":"badge-rose",
     "tema":"Prefill vs Decode. KV Cache, PagedAttention. Nsight Compute / PyTorch Profiler. Benchmarking.",
     "obj":"Ser capaz de perfilar modelos, encontrar cuellos de botella reales y reportar métricas rigurosas.",
     "prac":"Perfilar un script con PyTorch Profiler, identificar cuello de botella y documentarlo.",
     "lec":"Kwon et al. (2023) — vLLM · Reagen et al. — Efficient ML Benchmarking"},
]

# ---------------------------------------------------------
# SIDEBAR
# ---------------------------------------------------------
with st.sidebar:
    st.markdown("""
        <div style='text-align:center; padding: 16px 0 8px 0;'>
            <div style='font-size:2.6rem; filter: drop-shadow(0 0 12px rgba(34,211,238,0.6));'>🚀</div>
            <div style='font-weight:900; font-size:1.25rem; letter-spacing:-0.02em;
                        background: linear-gradient(90deg,#22d3ee,#c084fc);
                        -webkit-background-clip:text; -webkit-text-fill-color:transparent;'>
                SIMG · 2026
            </div>
            <div style='color:#64748b; font-size:0.78rem; margin-top:2px; letter-spacing:0.05em;'>
                HPC &nbsp;·&nbsp; IA GENERATIVA
            </div>
        </div>
    """, unsafe_allow_html=True)

    st.markdown("---")

    opciones = [
        "🏠 Inicio",
        "🎯 Enfoque y metodología",
        "🗺️ Roadmap del semestre",
        "🎓 Cierre",
    ]
    seleccion = st.radio("Navegación", opciones, label_visibility="collapsed")

    st.markdown("---")
    if lottie_cpu:
        st_lottie(lottie_cpu, height=110, key="sb_lottie")

    st.markdown(
        "<div style='text-align:center; color:#475569; font-size:0.72rem; line-height:1.5;'>"
        "Universidad Nacional de Colombia<br>Facultad de Ciencias</div>",
        unsafe_allow_html=True
    )

# ═════════════════════════════════════════════════════════
# VISTA: INICIO
# ═════════════════════════════════════════════════════════
if seleccion == "🏠 Inicio":

    col1, col2 = st.columns([2.4, 1])
    with col1:
        st.markdown("<div class='neon-title fade-in'>Semillero de HPC<br>en Modelos Generativos</div>", unsafe_allow_html=True)
        st.markdown("<div class='subtitle fade-in'>Donde el rendimiento computacional se encuentra con la IA moderna.</div>", unsafe_allow_html=True)
        st.write("")
        st.markdown("""
        En **SIMG** estudiamos **cómo se entrenan, optimizan e implementan** los modelos generativos
        que hoy definen la frontera de la IA. No nos quedamos en la arquitectura: bajamos al
        **kernel, la memoria y la red** para entender *por qué* un modelo es rápido, lento o imposible de escalar.
        """)
    with col2:
        if lottie_ai:
            st_lottie(lottie_ai, height=190, key="home_ai")

    st.write("")

    k1, k2, k3, k4 = st.columns(4)
    kpis = [
        ("Sesiones del semestre", "10", "📚"),
        ("Enfoque del semestre",   "Divulgar", "📣"),
        ("Compromiso mínimo",      "90%", "✅"),
        ("Papers de referencia",   "12+", "📄"),
    ]
    for col, (label, value, icon) in zip([k1, k2, k3, k4], kpis):
        with col:
            st.markdown(f"""
                <div class="kpi fade-in">
                    <div class="kpi-label">{icon} {label}</div>
                    <div class="kpi-value">{value}</div>
                </div>
            """, unsafe_allow_html=True)

    st.write("")
    st.write("")
    st.markdown("### 🎯 Los tres pilares del semestre")

    p1, p2, p3 = st.columns(3)
    with p1:
        st.markdown("""
            <div class="pillar fade-in" style="animation-delay:0.05s;">
                <div class="pillar-icon">🧠</div>
                <div class="pillar-title">Entender</div>
                <div class="pillar-text">
                    Comprender el cuello de botella real de cada modelo: no la arquitectura,
                    sino los <b>FLOPs</b>, la <b>VRAM</b> y el <b>ancho de banda</b>.
                </div>
            </div>
        """, unsafe_allow_html=True)
    with p2:
        st.markdown("""
            <div class="pillar fade-in" style="animation-delay:0.15s;">
                <div class="pillar-icon">⚡</div>
                <div class="pillar-title">Optimizar</div>
                <div class="pillar-text">
                    Escribir kernels, mezclar precisión, paralelizar y cuantizar.
                    Bajar del <code>model.fit()</code> a los hilos, warps y redes.
                </div>
            </div>
        """, unsafe_allow_html=True)
    with p3:
        st.markdown("""
            <div class="pillar fade-in" style="animation-delay:0.25s;">
                <div class="pillar-icon">📣</div>
                <div class="pillar-title">Divulgar</div>
                <div class="pillar-text">
                    Sesiones abiertas al público y grabadas. Cada tema se explica como
                    si el asistente fuera un ingeniero curioso, no un especialista.
                </div>
            </div>
        """, unsafe_allow_html=True)

    st.write("")
    st.write("")

    with st.container(border=True):
        st.markdown("#### 🌐 ¿Por qué HPC e IA generativa juntos?")
        st.markdown("""
        Los modelos que hoy usamos —LLMs, difusión, video generativo— **no son posibles sin HPC**.
        Cada avance algorítmico (FlashAttention, LoRA, FP8) es, en el fondo, una
        **decisión de HPC**. Este semillero une las dos mitades:

        - **HPC:** hardware, jerarquía de memoria, MPI/NCCL, paralelismo, profiling.
        - **IA generativa:** Transformers, difusión, VAEs, flow matching, despliegue.

        El resultado es una comunidad que entiende *qué hay debajo* del `pip install transformers`.
        """)

# ═════════════════════════════════════════════════════════
# VISTA: ENFOQUE Y METODOLOGÍA
# ═════════════════════════════════════════════════════════
elif seleccion == "🎯 Enfoque y metodología":

    st.markdown("<div class='neon-title sm fade-in'>Enfoque y metodología</div>", unsafe_allow_html=True)
    st.markdown("<div class='subtitle fade-in'>Cómo vamos a trabajar este semestre y por qué.</div>", unsafe_allow_html=True)
    st.write("")

    with st.container(border=True):
        st.markdown("### 📣 Enfoque del semestre: divulgación y estructura")
        st.markdown("""
        Este semestre el semillero cambia de ritmo. Además de aprender, vamos a
        **sistematizar y divulgar** lo que sabemos. Todas las sesiones serán:

        - **Abiertas al público** — cualquiera puede asistir.
        - **Grabadas** — quedarán como material consultable del semillero.
        - **Estructuradas** — cada sesión sigue una plantilla fija.
        - **Presentadas exclusivamente por miembros oficiales** del grupo.
        """)

    st.write("")

    st.markdown("### ⏱️ Estructura de una sesión")

    st.markdown("""
    <div class="session-tl fade-in">
        <div class="tl-seg cyan" style="flex: 30;">
            <div class="lbl">📖 Lectura y discusión</div>
            <div class="min">30 min · máx</div>
        </div>
        <div class="tl-seg indigo" style="flex: 90;">
            <div class="lbl">🧠 Presentación técnica</div>
            <div class="min">20 min – 1 h 30</div>
        </div>
        <div class="tl-seg pink" style="flex: 15;">
            <div class="lbl">🎮 Kahoot</div>
            <div class="min">15 min</div>
        </div>
    </div>
    <div class="tl-total">
        <span>Antes de cada presentación se lee el abstract y resultados principales del paper asignado.</span>
        <span>Duración total: <strong>≈ 2h 15m</strong></span>
    </div>
    """, unsafe_allow_html=True)

    st.write("")
    st.write("")

    st.markdown("### 🤝 Compromisos y reglas")

    c1, c2 = st.columns(2)
    with c1:
        with st.container(border=True):
            st.markdown("#### ✅ Asistencia")
            st.markdown("""
            - Mínimo **90 % de asistencia** al semestre.
            - Inasistencias válidas **solo** con justificación previa.
            - La constancia es lo que sostiene un semillero: sin quórum, no hay discusión.
            """)
        with st.container(border=True):
            st.markdown("#### 🎤 Presentaciones")
            st.markdown("""
            - Exclusivamente por **miembros oficiales** del grupo.
            - Modalidad **presencial** (sujeta a aprobación del líder).
            - Cada expositor prepara su **Kahoot** de cierre.
            """)
    with c2:
        with st.container(border=True):
            st.markdown("#### 🤗 Socialización")
            st.markdown("""
            Durante la **segunda sesión** (después de apertura y conceptos clave)
            se reserva un espacio final para conocer a cada miembro y a los nuevos postulantes.
            """)
        with st.container(border=True):
            st.markdown("#### 🎓 Sesión de experto")
            st.markdown("""
            A lo largo del semestre invitaremos a un **profesor o experto** del área
            para dictar una sesión especial o un tema afín de alta relevancia.
            """)

# ═════════════════════════════════════════════════════════
# VISTA: ROADMAP (timeline en dos columnas)
# ═════════════════════════════════════════════════════════
elif seleccion == "🗺️ Roadmap del semestre":

    st.markdown("<div class='neon-title sm fade-in'>Roadmap del Semestre</div>", unsafe_allow_html=True)
    st.markdown("<div class='subtitle fade-in'>De los fundamentos a la inferencia eficiente, sesión por sesión.</div>", unsafe_allow_html=True)
    st.write("")

    col_l, col_r = st.columns(2)
    for i, s in enumerate(sesiones):
        target = col_l if i % 2 == 0 else col_r
        with target:
            st.markdown(f"""
                <div class="tl-item fade-in" style="animation-delay:{i*0.05}s;">
                    <div class="tl-num">SESIÓN {s['n']}</div>
                    <div class="tl-title">{s['icon']} {s['title']}</div>
                    <div class="tl-sub">{s['sub']}</div>
                    <div style="margin-top:6px;">
                        <span class="badge {s['badge']}">{s['tag']}</span>
                    </div>
                </div>
            """, unsafe_allow_html=True)

# ═════════════════════════════════════════════════════════
# VISTA: CIERRE
# ═════════════════════════════════════════════════════════
elif seleccion == "🎓 Cierre":
    st.write("")
    st.write("")
    st.markdown("""
        <div style='text-align:center; animation: fadeUp 1s ease both;'>
            <div style='font-size:3rem; font-weight:900; letter-spacing:-0.03em;
                        background: linear-gradient(90deg,#22d3ee,#818cf8,#c084fc);
                        -webkit-background-clip:text; -webkit-text-fill-color:transparent;'>
                ¡Listos para exprimir el silicio!
            </div>
            <div style='color:#94a3b8; font-size:1.15rem; margin-top:14px; max-width:720px; margin-left:auto; margin-right:auto; line-height:1.6;'>
                El cuello de botella de la IA hoy no son las ideas — son los <b style="color:#22d3ee;">FLOPs</b>,
                la <b style="color:#818cf8;">VRAM</b> y el <b style="color:#c084fc;">ancho de banda</b>.<br>
                En SIMG aprendemos a romper esas barreras.
            </div>
        </div>
    """, unsafe_allow_html=True)

    c1, c2, c3 = st.columns([1, 1.4, 1])
    with c2:
        if lottie_rocket:
            st_lottie(lottie_rocket, height=280, key="rocket")

    st.markdown("""
        <div style='text-align:center; color:#64748b; margin-top:10px; line-height:1.7;'>
            <b style='color:#22d3ee;'>SIMG</b> · Semillero de HPC en Modelos Generativos<br>
            <i>Universidad Nacional de Colombia · Facultad de Ciencias</i>
        </div>
    """, unsafe_allow_html=True)

    st.balloons()