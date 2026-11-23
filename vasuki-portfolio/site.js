(() => {
  "use strict";

  const root = document.documentElement;
  const header = document.querySelector(".site-header");
  const mainNav = document.querySelector(".main-nav");
  const menu = document.querySelector(".menu-toggle");
  const menuLabel = menu.querySelector(".menu-label");
  const narrow = window.matchMedia("(max-width: 53rem)");
  const motion = window.matchMedia("(prefers-reduced-motion: reduce)");

  function setMenu(open, returnFocus = false) {
    menu.setAttribute("aria-expanded", String(open));
    menu.setAttribute("aria-label", open ? "Close navigation" : "Open navigation");
    menuLabel.textContent = open ? "Close" : "Menu";
    mainNav.classList.toggle("is-open", open);
    if (returnFocus) menu.focus();
  }

  menu.addEventListener("click", () => {
    setMenu(menu.getAttribute("aria-expanded") !== "true");
  });
  mainNav.addEventListener("click", (event) => {
    const link = event.target.closest("a");
    if (!link) return;
    const mobileOpen = menu.getAttribute("aria-expanded") === "true";
    setMenu(false);
    if (mobileOpen && link.hash && document.querySelector(link.hash)) {
      const target = document.querySelector(link.hash);
      target.setAttribute("tabindex", "-1");
      target.focus({ preventScroll: true });
    }
  });
  document.addEventListener("click", (event) => {
    if (!header.contains(event.target)) setMenu(false);
  });
  document.addEventListener("focusin", (event) => {
    if (!header.contains(event.target)) setMenu(false);
  });
  document.addEventListener("keydown", (event) => {
    if (event.key === "Escape" && menu.getAttribute("aria-expanded") === "true") {
      setMenu(false, true);
    }
  });
  narrow.addEventListener("change", () => setMenu(false));
  root.classList.add("enhanced");

  const sections = Array.from(document.querySelectorAll("main [data-nav]"));
  const links = Array.from(mainNav.querySelectorAll("[data-section]"));
  const heroImage = document.querySelector(".hero-art-img");
  if (sections.length) {
    let frame = 0;
    let current = "";

    function updatePosition() {
      frame = 0;
      const threshold = header.offsetHeight + Math.min(window.innerHeight * .22, 160);
      let active = sections[0].dataset.nav;
      for (const section of sections) {
        if (section.getBoundingClientRect().top <= threshold) active = section.dataset.nav;
        else break;
      }
      if (active !== current) {
        current = active;
        for (const link of links) {
          if (link.dataset.section === active) link.setAttribute("aria-current", "location");
          else link.removeAttribute("aria-current");
        }
      }
      if (heroImage && !motion.matches && !narrow.matches && window.scrollY < window.innerHeight) {
        const offset = Math.min(16, Math.max(0, window.scrollY * .055));
        heroImage.style.transform = "translateY(" + offset.toFixed(1) + "px)";
      } else if (heroImage && heroImage.style.transform) {
        heroImage.style.transform = "";
      }
    }

    function schedulePosition() {
      if (!frame) frame = window.requestAnimationFrame(updatePosition);
    }
    window.addEventListener("scroll", schedulePosition, { passive: true });
    window.addEventListener("resize", schedulePosition);
    window.addEventListener("pageshow", schedulePosition);
    motion.addEventListener("change", schedulePosition);
    updatePosition();
  }

  if ("IntersectionObserver" in window && !motion.matches) {
    const reveal = new IntersectionObserver((entries, observer) => {
      for (const entry of entries) {
        if (!entry.isIntersecting) continue;
        entry.target.classList.add("just-visible");
        observer.unobserve(entry.target);
      }
    }, { threshold: .15 });
    for (const title of document.querySelectorAll("[data-reveal]")) reveal.observe(title);
  }

  const dialog = document.querySelector("#study-dialog");
  if (!dialog) return;
  const studies = Array.from(document.querySelectorAll(".study-open"));
  const largeImage = dialog.querySelector(".dialog-image");
  const heading = dialog.querySelector("#study-dialog-title");
  const description = dialog.querySelector(".dialog-description");
  const close = dialog.querySelector(".dialog-close");
  let studyIndex = 0;
  let opener = null;

  function selectStudy(index) {
    studyIndex = (index + studies.length) % studies.length;
    const item = studies[studyIndex].closest(".study");
    const image = item.querySelector("img");
    largeImage.src = image.src;
    largeImage.alt = image.alt;
    heading.textContent = item.querySelector("figcaption").textContent;
    description.textContent = item.querySelector(".study-description").textContent;
  }

  for (const button of studies) {
    button.addEventListener("click", (event) => {
      if (event.ctrlKey || event.metaKey || event.shiftKey || event.altKey || typeof dialog.showModal !== "function") return;
      event.preventDefault();
      opener = button;
      selectStudy(Number(button.dataset.study));
      dialog.showModal();
      document.body.classList.add("dialog-active");
      close.focus();
    });
  }
  close.addEventListener("click", () => dialog.close());
  dialog.addEventListener("close", () => {
    document.body.classList.remove("dialog-active");
    if (opener) opener.focus({ preventScroll: true });
  });
  dialog.addEventListener("click", (event) => {
    if (event.target !== dialog) return;
    const box = dialog.getBoundingClientRect();
    if (event.clientX < box.left || event.clientX > box.right ||
        event.clientY < box.top || event.clientY > box.bottom) dialog.close();
  });
  dialog.addEventListener("keydown", (event) => {
    if (event.key === "ArrowLeft" || event.key === "ArrowRight") {
      event.preventDefault();
      selectStudy(studyIndex + (event.key === "ArrowLeft" ? -1 : 1));
    }
  });
  dialog.querySelector(".prev-study").addEventListener("click", () => selectStudy(studyIndex - 1));
  dialog.querySelector(".next-study").addEventListener("click", () => selectStudy(studyIndex + 1));
})();
