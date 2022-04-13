{{ $requiredArgs := (slice "fname") }}

{{ range $requiredArgs }}
  {{ with ($.Get .) }}{{ else }}{{ errorf "missing argument %s" . }}{{ end }}
{{ end }}

``````````````````````````````````````{{ with (.Get "lang") }}{{ . }}{{ end }}
{{ printf "%s" (readFile (.Get "fname")) | safeHTML }}
``````````````````````````````````````
