// Public configuration only. Override with window.AL_MAHER_CONFIG before app.js.
// Never place credentials here. Production API and website must share an HTTPS origin.
export const config = Object.freeze({
  production: false, apiBase: '', siteUrl: '', analyticsMeasurementId: '',
  googleTagManagerId: '', metaPixelId: '', googleAdsId: '', googleAdsConversionLabel: '',
  verifiedMapEmbedUrl: '', verifiedDirectionsUrl: '', businessProfileUrl: '', openingHours: null,
  ...globalThis.AL_MAHER_CONFIG
});
