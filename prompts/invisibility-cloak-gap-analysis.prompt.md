# Invisibility Cloak Gap Analysis
<!---
   <category>prompt-engineering</category>
   <models>
      <model>any</model>
   </models>
   <tags>
      <tag>gap-analysis</tag>
      <tag>strategic-audit</tag>
      <tag>content-review</tag>
   </tags>
   <description>Framework to surface the five most consequential missing elements in a document by decomposing structure, building a requirements touchstone, and producing a concise gap table with actionable example passages.</description>
   <version>1.0.0</version>
   <language>en</language>
   <status>stable</status>
   <created>2025-06-27</created>
   <updated>2025-06-27</updated>
   <author>Allie K. Miller</author>
   <license></license>
-->
```markdown
You are a top 0.01% strategic auditor.

<objective>  
Expose the five most consequential content gaps in [attached doc].
</objective>

<execution framework>  
1. DECOMPOSE — Break the document into its logical sections and outline the information architecture.  
2. TOUCHSTONE BUILD — Draft a requirements matrix grounded in domain best practices, stakeholder needs, and obvious topical dimensions (e.g., regions, use-cases, modalities).
</execution framework>  

<output table>
| Missing Element | Description and What It Should Cover | Example Passage (match tone and style of report) | Likely Reason for Omission |
</output table>

<guidelines>  
• Keep your internal notes private; show only the table and a brief recommendation paragraph.  
• Match the document’s voice exactly in the “Example Passage” column.  
• Focus on strategic content omissions—missing geographies, sub-topics, modalities, stakeholder perspectives—not code, data pipelines, or system architecture.  
• Cap each table cell at ≈ 60 words for crisp readability.
</guidelines>  
```
