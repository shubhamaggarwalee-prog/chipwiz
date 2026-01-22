import React, { useState, useEffect } from 'react';
import { Link, useParams } from 'react-router-dom';
import { reportsApi } from '../lib/api';
import { Button } from '../components/ui/button';
import { 
  FileText, 
  Download, 
  ChevronRight,
  Clock,
  Filter,
  User,
  AlertTriangle
} from 'lucide-react';

const ReportsPage = () => {
  const { slug } = useParams();
  const [reports, setReports] = useState([]);
  const [reportTypes, setReportTypes] = useState([]);
  const [selectedReport, setSelectedReport] = useState(null);
  const [selectedType, setSelectedType] = useState('');
  const [loading, setLoading] = useState(true);

  // Fetch report types
  useEffect(() => {
    const fetchTypes = async () => {
      try {
        const response = await reportsApi.getTypes();
        setReportTypes(response.data);
      } catch (error) {
        console.error('Error fetching types:', error);
      }
    };
    fetchTypes();
  }, []);

  // Fetch reports
  useEffect(() => {
    const fetchReports = async () => {
      setLoading(true);
      try {
        const params = {};
        if (selectedType) params.report_type = selectedType;
        
        const response = await reportsApi.getReports(params);
        setReports(response.data);
      } catch (error) {
        console.error('Error fetching reports:', error);
      } finally {
        setLoading(false);
      }
    };
    fetchReports();
  }, [selectedType]);

  // Fetch single report
  useEffect(() => {
    const fetchReport = async () => {
      if (!slug) {
        setSelectedReport(null);
        return;
      }
      
      try {
        const response = await reportsApi.getReport(slug);
        setSelectedReport(response.data);
      } catch (error) {
        console.error('Error fetching report:', error);
      }
    };
    fetchReport();
  }, [slug]);

  // Report detail view
  if (selectedReport) {
    return (
      <div className="min-h-screen bg-slate-50 dark:bg-slate-900" data-testid="report-detail-page">
        <div className="container-app py-8">
          <Link 
            to="/reports" 
            className="inline-flex items-center gap-2 text-sm text-slate-600 hover:text-slate-900 mb-6 dark:text-slate-400 dark:hover:text-white"
          >
            <ChevronRight className="h-4 w-4 rotate-180" />
            Back to Reports
          </Link>

          <article className="card-base p-6 lg:p-10 max-w-4xl mx-auto">
            {/* Header */}
            <div className="mb-8 pb-6 border-b border-slate-200 dark:border-slate-700">
              <div className="flex items-center gap-3 mb-4">
                <span className="px-3 py-1 bg-blue-50 text-blue-600 rounded-full text-sm font-medium dark:bg-blue-900/30 dark:text-blue-400">
                  {reportTypes.find(t => t.id === selectedReport.report_type)?.name || selectedReport.report_type}
                </span>
                {selectedReport.premium_only && (
                  <span className="px-3 py-1 bg-yellow-50 text-yellow-600 rounded-full text-sm font-medium dark:bg-yellow-900/30 dark:text-yellow-400">
                    Premium
                  </span>
                )}
              </div>

              <h1 className="text-3xl lg:text-4xl font-semibold mb-4">{selectedReport.title}</h1>
              
              <div className="flex flex-wrap items-center gap-4 text-sm text-slate-500">
                <span className="flex items-center gap-1">
                  <User className="h-4 w-4" />
                  {selectedReport.author}
                </span>
                <span className="flex items-center gap-1">
                  <Clock className="h-4 w-4" />
                  {new Date(selectedReport.created_at).toLocaleDateString()}
                </span>
              </div>
            </div>

            {/* Executive Summary */}
            <section className="mb-8">
              <h2 className="text-xl font-semibold mb-4">Executive Summary</h2>
              <div className="p-6 bg-slate-50 rounded-xl whitespace-pre-wrap dark:bg-slate-800">
                {selectedReport.executive_summary}
              </div>
            </section>

            {/* Content Sections */}
            {selectedReport.content_sections?.map((section, i) => (
              <section key={i} className="mb-8">
                <h2 className="text-xl font-semibold mb-4">{section.title}</h2>
                <div className="prose-semi whitespace-pre-wrap">
                  {section.content?.split('\n').map((line, j) => {
                    if (line.startsWith('## ')) {
                      return <h3 key={j} className="text-lg font-medium mt-6 mb-3">{line.replace('## ', '')}</h3>;
                    }
                    if (line.startsWith('### ')) {
                      return <h4 key={j} className="font-medium mt-4 mb-2">{line.replace('### ', '')}</h4>;
                    }
                    if (line.startsWith('| ')) {
                      return <div key={j} className="font-mono text-sm bg-slate-50 p-2 my-1 dark:bg-slate-800">{line}</div>;
                    }
                    if (line.startsWith('- ')) {
                      return <li key={j} className="ml-4">{line.replace('- ', '')}</li>;
                    }
                    if (line.trim()) {
                      return <p key={j} className="mb-3">{line}</p>;
                    }
                    return null;
                  })}
                </div>
              </section>
            ))}

            {/* Data Sources */}
            {selectedReport.data_sources?.length > 0 && (
              <section className="mb-8">
                <h2 className="text-xl font-semibold mb-4">Data Sources</h2>
                <ul className="list-disc pl-6 space-y-2 text-slate-600 dark:text-slate-400">
                  {selectedReport.data_sources.map((source, i) => (
                    <li key={i}>{source}</li>
                  ))}
                </ul>
              </section>
            )}

            {/* Assumptions */}
            {selectedReport.assumptions?.length > 0 && (
              <section className="mb-8 p-6 bg-yellow-50 rounded-xl dark:bg-yellow-900/20">
                <h2 className="text-lg font-semibold mb-3 flex items-center gap-2 text-yellow-700 dark:text-yellow-400">
                  <AlertTriangle className="h-5 w-5" />
                  Assumptions
                </h2>
                <ul className="list-disc pl-6 space-y-2 text-yellow-800 dark:text-yellow-300">
                  {selectedReport.assumptions.map((assumption, i) => (
                    <li key={i}>{assumption}</li>
                  ))}
                </ul>
              </section>
            )}

            {/* Risks & Unknowns */}
            {selectedReport.risks_unknowns?.length > 0 && (
              <section className="mb-8 p-6 bg-red-50 rounded-xl dark:bg-red-900/20">
                <h2 className="text-lg font-semibold mb-3 flex items-center gap-2 text-red-700 dark:text-red-400">
                  <AlertTriangle className="h-5 w-5" />
                  Risks & Unknowns
                </h2>
                <ul className="list-disc pl-6 space-y-2 text-red-800 dark:text-red-300">
                  {selectedReport.risks_unknowns.map((risk, i) => (
                    <li key={i}>{risk}</li>
                  ))}
                </ul>
              </section>
            )}

            {/* References */}
            {selectedReport.references?.length > 0 && (
              <section className="mb-8">
                <h2 className="text-xl font-semibold mb-4">References</h2>
                <div className="space-y-2">
                  {selectedReport.references.map((ref, i) => (
                    <a
                      key={i}
                      href={ref.url}
                      target="_blank"
                      rel="noopener noreferrer"
                      className="block p-3 rounded-lg hover:bg-slate-50 transition-colors dark:hover:bg-slate-800"
                    >
                      <p className="text-blue-600 hover:text-blue-700">{ref.title}</p>
                      <p className="text-xs text-slate-500">{ref.source}</p>
                    </a>
                  ))}
                </div>
              </section>
            )}

            {/* Disclaimer */}
            <div className="mt-8 pt-6 border-t border-slate-200 dark:border-slate-700">
              <p className="text-xs text-slate-500 text-center">
                This report is based on publicly available information and AI-assisted analysis. 
                It does not constitute investment advice. Verify critical information with primary sources.
              </p>
            </div>
          </article>
        </div>
      </div>
    );
  }

  return (
    <div className="min-h-screen bg-slate-50 dark:bg-slate-900" data-testid="reports-page">
      <div className="container-app py-8">
        {/* Header */}
        <div className="flex flex-col md:flex-row md:items-center md:justify-between gap-4 mb-8">
          <div>
            <h1 className="text-3xl font-semibold mb-2">Research Reports</h1>
            <p className="text-slate-600 dark:text-slate-400">
              TechInsights-style analysis based on public sources
            </p>
          </div>
        </div>

        {/* Type Filter */}
        <div className="flex flex-wrap gap-2 mb-8">
          <Button
            variant={selectedType === '' ? 'default' : 'outline'}
            size="sm"
            onClick={() => setSelectedType('')}
            data-testid="type-all"
          >
            All Reports
          </Button>
          {reportTypes.map((type) => (
            <Button
              key={type.id}
              variant={selectedType === type.id ? 'default' : 'outline'}
              size="sm"
              onClick={() => setSelectedType(type.id)}
              data-testid={`type-${type.id}`}
            >
              {type.name}
            </Button>
          ))}
        </div>

        {/* Reports Grid */}
        {loading ? (
          <div className="flex items-center justify-center h-64">
            <div className="w-8 h-8 border-4 border-blue-600 border-t-transparent rounded-full animate-spin"></div>
          </div>
        ) : reports.length > 0 ? (
          <div className="grid md:grid-cols-2 gap-6">
            {reports.map((report) => (
              <Link
                key={report.report_id}
                to={`/reports/${report.slug}`}
                className="card-base p-6 hover:-translate-y-1 transition-all duration-300"
                data-testid={`report-${report.slug}`}
              >
                <div className="flex items-center gap-3 mb-3">
                  <span className="px-2 py-0.5 bg-blue-50 text-blue-600 text-xs rounded dark:bg-blue-900/30 dark:text-blue-400">
                    {reportTypes.find(t => t.id === report.report_type)?.name || report.report_type}
                  </span>
                  {report.premium_only && (
                    <span className="px-2 py-0.5 bg-yellow-50 text-yellow-600 text-xs rounded dark:bg-yellow-900/30 dark:text-yellow-400">
                      Premium
                    </span>
                  )}
                </div>
                
                <h3 className="text-lg font-medium mb-2">{report.title}</h3>
                <p className="text-sm text-slate-600 dark:text-slate-400 line-clamp-3 mb-4">
                  {report.executive_summary}
                </p>
                
                <div className="flex items-center justify-between text-sm text-slate-500">
                  <span className="flex items-center gap-1">
                    <User className="h-4 w-4" />
                    {report.author}
                  </span>
                  <span className="flex items-center gap-1">
                    <Clock className="h-4 w-4" />
                    {new Date(report.created_at).toLocaleDateString()}
                  </span>
                </div>
              </Link>
            ))}
          </div>
        ) : (
          <div className="text-center py-16">
            <FileText className="h-16 w-16 text-slate-300 mx-auto mb-4" />
            <h3 className="text-lg font-medium mb-2">No reports available</h3>
            <p className="text-slate-600 dark:text-slate-400">
              Research reports are being generated. Check back soon.
            </p>
          </div>
        )}
      </div>
    </div>
  );
};

export default ReportsPage;
