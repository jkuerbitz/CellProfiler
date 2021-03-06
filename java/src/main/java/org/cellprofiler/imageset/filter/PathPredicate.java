/**
 * CellProfiler is distributed under the GNU General Public License.
 * See the accompanying file LICENSE for details.
 *
 * Copyright (c) 2003-2009 Massachusetts Institute of Technology
 * Copyright (c) 2009-2013 Broad Institute
 * All rights reserved.
 * 
 * Please see the AUTHORS file for credits.
 * 
 * Website: http://www.cellprofiler.org
 */
package org.cellprofiler.imageset.filter;

import org.cellprofiler.imageset.ImageFile;

/**
 * @author Lee Kamentsky
 *
 */
public class PathPredicate extends AbstractURLPredicate {
	final static public String SYMBOL = "directory";
	/* (non-Javadoc)
	 * @see org.cellprofiler.imageset.filter.FilterPredicate#getSymbol()
	 */
	public String getSymbol() {
		return SYMBOL;
	}
	/* (non-Javadoc)
	 * @see org.cellprofiler.imageset.filter.AbstractURLPredicate#getValue(org.cellprofiler.imageset.ImageFile)
	 */
	@Override
	protected String getValue(ImageFile candidate) {
		return candidate.getPathName();
	}

}
